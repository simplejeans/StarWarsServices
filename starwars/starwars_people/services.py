from abc import ABC

import petl

from starwars_people.adapters import StarWarsAdapters
from starwars_people.clients import StarWarsApiClient
from starwars_people.models import Dataset
from starwars_people.utils import generate_unique_name
from django.core.files import File
import os


class DataWriterDBSaver(ABC):
    file_name = None
    client = StarWarsApiClient()

    def write_data_and_save_to_file(self):
        pass

    def save_file_to_db_and_remove_from_disc(self):
        pass


class CSVDataWriterAndDBSaver(DataWriterDBSaver):

    def __init__(self):
        self.file_name = generate_unique_name()
        self.adapter = StarWarsAdapters()

    def write_data_and_save_to_file(self):
        data = self.adapter.save_all_filtering(people_data=self.client.get_people_data(), planets_data=self.client.get_planets_data())
        csv_header = data[0].keys()
        csv_table = [csv_header]

        for row in data:
            csv_row = [row[row_name] for row_name in csv_header]
            csv_table.append(csv_row)

        petl.tocsv(csv_table, f'{self.file_name}.csv', encoding="utf-8")

    def save_file_to_db_and_remove_from_disc(self):
        with open(f'{self.file_name}.csv', 'r') as dataset_file:
            Dataset.objects.create(file=File(dataset_file), file_name=self.file_name)

        os.remove(f'{self.file_name}.csv')


