from requests import request, Response


class StarWarsApiClient:

    people_url = "https://swapi.py4e.com/api/people"
    planets_url = "https://swapi.py4e.com/api/planets/"

    @staticmethod
    def client(method: str, url: str, headers: dict, json: dict) -> Response:
        return request(method=method, url=url, headers=headers, json=json)

    def get_people_data(self):
        people_data = []
        url = self.people_url
        while True:
            response = self.client("get", url, headers={}, json={})
            response = response.json()
            people_data.extend(response['results'])
            if response['next'] is None:
                break
            url = response['next']

        return people_data

    def get_planets_data(self):
        planets_data = []
        url = self.planets_url
        while True:
            response = self.client("get", url, headers={}, json={})
            response = response.json()
            planets_data.extend(response['results'])
            if response['next'] is None:
                break
            url = response['next']

        return planets_data
