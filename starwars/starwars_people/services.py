from abc import ABC
from csv import DictWriter

import petl
from starwars.settings import BASE_DIR
from starwars_people.adapters import StarWarsAdapters
from starwars_people.clients import StarWarsApiClient
from starwars_people.models import Dataset
from starwars_people.utils import generate_unique_name
from django.core.files import File
import os

adapter = StarWarsAdapters()
client = StarWarsApiClient()
people_data = client.get_people_data()
planets_data = client.get_planets_data()
data = adapter.adapt(people_data=people_data, planets_data=planets_data)


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

    def _write_data_and_save_to_file(self):
        keys = data[0].keys()
        with open(f'{self.file_name}.csv', 'w+') as dataset_file:
            writer = DictWriter(dataset_file, keys)
            writer.writeheader()
            writer.writerows(data)

    def _save_file_to_db_and_remove_from_disc(self):
        with open(f'{self.file_name}.csv', 'r') as dataset_file:
            Dataset.objects.create(file=File(dataset_file), file_name=self.file_name)

        os.remove(f'{self.file_name}.csv')

    def write_data_to_db_and_remove_from_disk(self):
        self._write_data_and_save_to_file()
        self._save_file_to_db_and_remove_from_disc()


def get_csv_file_from_db(file_name):
    root = os.path.join(BASE_DIR, 'datasets', f'{file_name}.csv')
    with open(root, 'r') as csv_file:
        file = csv_file.readlines()
        return file


def make_pagination(file_name):
    file = get_csv_file_from_db(file_name=file_name)
    for i in range(0, len(file), 10):
        yield file[i:i + 10]
