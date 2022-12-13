from datetime import datetime

from starwars_people.clients import StarWarsApiClient


class StarWarsAdapters:

    planets = {}

    def change_homeworld_column(self, person: dict):
        person['homeworld'] = self.planets[person["homeworld"]]

    def planets_data_adapter(self, planets_data: dict):
        for planet in planets_data:
            self.planets[planet['url']] = planet['name']

    def add_data_column(self, person: dict):
        edited_column = person['edited']
        datetime_object = datetime.strptime(edited_column, "%Y-%m-%dT%H:%M:%S.%fZ")
        data_column_format = datetime_object.strftime("%Y-%m-%d")
        person['date'] = data_column_format

    def drop_columns(self, person: dict) -> dict:
        requires_columns = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
                            'gender', 'homeworld', 'date']

        return {key: value for key, value in person.items() if key in requires_columns}

    def save_all_filtering(self, planets_data: dict, people_data: dict):
        self.planets_data_adapter(planets_data)
        required_people_data = []
        for person in people_data:
            self.change_homeworld_column(person)
            self.add_data_column(person)
            some_person = self.drop_columns(person)
            required_people_data.append(some_person)
        return required_people_data

