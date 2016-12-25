from django.test import TestCase, Client
from django.shortcuts import reverse
import faker
from . import factories

class ProfileTest(TestCase):
    def setUp(self):
        client = Client()
        self.user = factories.HousingUserFactory()
        self.listings = factories.ListingFactory.create_batch(listing_owner=self.user, size=5)

        client.force_login(self.user)

        self.profile_url = reverse('listings:profile')
        self.response = client.get(self.profile_url)


    def get_edit_listing_url(self, listing):
        return reverse('listings:edit', kwargs={"listing_id": listing.pk})

    def test_get_listings(self):
        for listing in self.user.get_listings:
            self.assertIn(listing, self.listings)

    def test_return_status_is_successful(self):
        self.assertEquals(self.response.status_code, 200)

    def test_edit_listing_url_renders(self):
        for listing in self.listings:
            url = self.get_edit_listing_url(listing)
            content = str(self.response.content)

            self.assertIn(url, content)
