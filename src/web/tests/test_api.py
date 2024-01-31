from .factories import (UserFactory, PlantFactory)

from rest_framework.test import APITestCase
from django.urls import reverse
import json


class TestPlantAPIView(APITestCase):
    def setUp(self):
        self.url = reverse("plant-list") # use the view url from the admin docs
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
        }]}

        response_data = json.loads(response.content)

        self.assertEqual(expected_content['results'][0]['id'], response_data['results'][0]['id'])
        self.assertEqual(expected_content['results'][0]['location'], response_data['results'][0]['location'])
        self.assertEqual(expected_content['results'][0]['name'], response_data['results'][0]['name'])


