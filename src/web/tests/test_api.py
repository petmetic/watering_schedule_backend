import json

from django.urls import reverse
from rest_framework.test import APITestCase

from web.tests.factories import PlantFactory, UserFactory


class TestPlantAPIView(APITestCase):
    def setUp(self):
        self.url_get = reverse("plant-list")  # use the view url from the admin docs
        self.url_post = reverse("plant-list")  # use the view url from the admin docs
        self.plant = PlantFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_get(self):
        response = self.client.get(self.url_get)
        print(f"response get: {response.content}")
        response.render()
        self.assertEquals(200, response.status_code)

        expected_content = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.plant.id,
                    "name": self.plant.name,
                    "location": "bedroom1",
                    "frequency": self.plant.frequency,
                    "volume": "100_ml",
                    "instructions": self.plant.instructions,
                    "start": self.plant.start,
                    "end": self.plant.end,
                    "status": "needs_watering",
                    "photo": self.plant.photo,
                }
            ],
        }

        response_data = json.loads(response.content)

        id_expected = expected_content["results"][0]["id"]
        id_api = response_data["results"][0]["id"]

        location_expected = expected_content["results"][0]["location"]
        location_api = response_data["results"][0]["location"]

        name_expected = expected_content["results"][0]["name"]
        name_api = response_data["results"][0]["name"]

        self.assertEqual(id_expected, id_api)
        self.assertEqual(location_expected, location_api)
        self.assertEqual(name_expected, name_api)

    def test_post(self):
        self.plant2 = PlantFactory.build(
            name="Pilea",
        )

        data = {
            "name": self.plant2.name,
            "location": self.plant2.location,
            "frequency": self.plant2.frequency,
            "volume": self.plant2.volume,
            "instructions": self.plant2.instructions,
            "photo": self.plant2.photo,
            "status": "needs_watering",
            "start": "2024-04-01T00:00:00+02:00",
            "end": "2024-04-30T00:00:00+02:00",
            "added": "2024-04-23T11:01:51.139599+02:00",
            "changed": "2024-04-23T11:01:51.139647+02:00",
        }

        expected_response_from_api = {
            "name": self.plant2.name,
            "location": self.plant2.location,
            "frequency": self.plant2.frequency,
            "volume": self.plant2.volume,
            "instructions": self.plant2.instructions,
        }

        resp = self.client.post(self.url_post, data=data)
        print(resp.content)
        self.assertEqual(resp.status_code, 201)
