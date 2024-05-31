import factory
import pytz
from django.contrib.auth.models import User

from web import models

tz = pytz.timezone("Europe/Ljubljana")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    username = factory.Sequence(lambda n: "Agent %03d" % n)
    email = factory.Sequence(lambda n: "Agent %03d" % n)


class PlantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Plant

    id = factory.Faker("pyint")
    name = factory.Faker("first_name")
    location = "bedroom1"
    frequency = factory.Faker("pyint")
    volume = "100_ml"
    instructions = factory.Faker("sentence")
    start = factory.Faker("date_time", tzinfo=tz)  # "%Y-%m-%d %H:%M:%S"
    end = factory.Faker("date_time", tzinfo=tz)  # "%Y-%m-%d %H:%M:%S"
    status = factory.Faker("pybool")
    photo = factory.django.ImageField(
        from_path="./web/tests/assets/placeholder_square_10-10.png",
        color="blue",
        width=200,
        height=200,
    )
