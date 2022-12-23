from datetime import datetime


class StarWarsAdapters:

    planets = {}

    def set_person_homeworld(self, person: dict):
        person['homeworld'] = self.planets[person["homeworld"]]

    def parse_planet_name(self, planets_data: dict):
        for planet in planets_data:
            self.planets[planet['url']] = planet['name']

    def set_date(self, person: dict):
        edited_column = person['edited']
        datetime_object = datetime.strptime(edited_column, "%Y-%m-%dT%H:%M:%S.%fZ")
        data_column_format = datetime_object.strftime("%Y-%m-%d")
        person['date'] = data_column_format

    def drop_redundant_columns(self, person: dict) -> dict:
        requires_columns = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year',
                            'gender', 'homeworld', 'date']

        return {key: value for key, value in person.items() if key in requires_columns}

    def adapt(self, planets_data: dict, people_data: dict):
        self.parse_planet_name(planets_data)
        required_people_data = []
        for person in people_data:
            self.set_person_homeworld(person)
            self.set_date(person)
            some_person = self.drop_redundant_columns(person)
            required_people_data.append(some_person)
        return required_people_data

