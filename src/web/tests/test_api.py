import json

from django.urls import reverse
from rest_framework.test import APITestCase

from web.tests.factories import PlantFactory, UserFactory


class TestPlantAPIView(APITestCase):
    def setUp(self):
        self.url = reverse("plant-list")  # use the view url from the admin docs
        self.plant = PlantFactory()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_get(self):
        response = self.client.get(self.url)
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
                    "photo": None,
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
