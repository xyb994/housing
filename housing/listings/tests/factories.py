import factory
from faker import Faker

fake = Faker()


class HousingUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'listings.HousingUser'


class ListingFactory(factory.django.DjangoModelFactory):
    lease_monthly_cost = fake.pyint()
    lease_deposit = fake.pyint()
    date_available = fake.date_time()
    bathroom_count = fake.pyint()
    bedroom_count = fake.pyint()
    unit_floor = fake.pyint()
    listing_owner = factory.SubFactory(HousingUserFactory)

    class Meta:
        model = 'listings.Listing'
