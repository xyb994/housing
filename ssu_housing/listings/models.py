# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

# from django.contrib.auth.models import AbstractUser
# from django.core.urlresolvers import reverse
# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _

from django.db import models
from ssu_housing.users.models import User
from django.dispatch import receiver
# from django.conf import settings

# Create your models here.
class HousingUser(models.Model):
    user = models.OneToOneField(User)

    @receiver(models.signals.post_save, sender=User)
    def create_housinguser(sender, instance, created, **kwargs):
        if created:
            HousingUser.objects.create(user=instance)

    @receiver(models.signals.post_save, sender=User)
    def save_housinguser(sender, instance, **kwargs):
        instance.housinguser.save()

    def get_listings(self):
        listings = self.listings_set.all.order_by(
            "-is_active", "-datetime_created")

        return listings

    def __str__(self):

        return self.user.email


class Listing(models.Model):
    FOR_RENT_BY_CHOICES = (
        ('owner', 'Owner'),
        ('management_company_or_broker', 'Management Company/Broker'),
        ('tenant', 'Tenant'),
    )

    LEASE_DURATION_CHOICES = (
        ('1_year', '1 Year'),
        ('6_months', '6 Months'),
        ('1_month', '1 Month'),
        ('sublet_temp', 'Sublet/Temporary'),
        ('other', 'Other(Please explain)'),
    )

    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'Apartments'),
        ('house', 'Houses'),
        ('homestay', 'Homestay'),
    )

    FURNISHED_CHOICES = (
        ('none', 'Unfurnished'),
        ('lightly_furnished', 'Lightly furnished'),
        ('fully_furnished', 'Fully furnished'),
    )

    PARKING_SPACE_COUNT_CHOICES = (
        ('0', 'None'),
        ('1', '1'),
        ('2', '2'),
        ('3_plus', '3+'),
    )

    PARKING_TYPE_CHOICES = (
        ('garage', 'Garage'),
        ('carport', 'Carport'),
        ('off_street', 'Off street'),
        ('other', 'Other'),
    )

    PET_ALLOWED_CHOICES = (
        ('no_pets_allowd', 'No pets allowed'),
        ('small', "Small"),
        ('big', 'Big'),
    )

    LAUNDRY_TYPE_CHOICES = (
        ('none', 'None'),
        ('in_unit', 'In-unit'),
        ('shared', 'Shared')
    )

    COOLING_CHOICES = (
        ('none', 'None'),
        ('air_conditioning', 'Air conditioning'),
        ('central_ac', 'Central A/C'),
    )

    listing_owner = models.ForeignKey(HousingUser, null=True)
    is_active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=9)
    for_rent_by = models.CharField(max_length=255, choices=FOR_RENT_BY_CHOICES)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    lease_monthly_cost = models.PositiveSmallIntegerField()
    lease_deposit = models.PositiveSmallIntegerField()
    lease_duration = models.CharField(max_length=255, choices=LEASE_DURATION_CHOICES)
    lease_duration_custom = models.CharField(max_length=128, blank=True, default='')
    date_available = models.DateField()
    additional_lease_terms = models.TextField(
        blank=True,
        help_text='Example: Owner pays for trash and sewer. Tenant responsible for gas and electric. Owner shovel snow, lawn, garden, driveway maintenance',
        default=''
    )
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    lease_whole_unit = models.BooleanField(default=False)
    owner_in_building = models.BooleanField(default=False)
    bedroom_count = models.PositiveSmallIntegerField()
    bathroom_count = models.PositiveSmallIntegerField()
    unit_sqft = models.PositiveSmallIntegerField(default=0)
    unit_floor = models.PositiveSmallIntegerField()
    furnished = models.CharField(max_length=17, choices=FURNISHED_CHOICES)
    furnished_details = models.CharField(blank=True, help_text='Furnishing detail, example: bed only...', default='', max_length=512)
    is_water_included = models.BooleanField(default=False)
    is_electricity_included = models.BooleanField(default=False)
    is_heat_included = models.BooleanField(default=False)
    is_internet_included = models.BooleanField(default=False)
    is_cable_included = models.BooleanField(default=False)
    parking_space_count = models.CharField(max_length=2, choices=PARKING_SPACE_COUNT_CHOICES)
    parking_type = models.CharField(max_length=10, choices=PARKING_TYPE_CHOICES)
    pet_allowed = models.CharField(max_length=14, choices=PET_ALLOWED_CHOICES)
    laundry_type = models.CharField(max_length=10, choices=LAUNDRY_TYPE_CHOICES)
    property_title = models.CharField(max_length=255, help_text='Example: [home stay 1 bedroom][apartment with 3 room][in-law apartment]', default='')
    property_description = models.TextField(blank=True, help_text='Example: above hill, driveway slippery, renting to international student for long time...A student from China/Moroco in one of room', default='')
    has_dishwasher = models.BooleanField(default=False)
    has_garbage_disposal = models.BooleanField(default=False)
    has_microwave = models.BooleanField(default=False)
    has_fridge = models.BooleanField(default=False)
    cooling = models.CharField(max_length=20, choices=COOLING_CHOICES)
    image1 = models.ImageField(upload_to='images', verbose_name='Image', blank=True)
    image2 = models.ImageField(upload_to='images', verbose_name='Image', blank=True)
    image3 = models.ImageField(upload_to='images', verbose_name='Image', blank=True)

    def __str__(self):

        return self.property_title

    class Meta:
        ordering = ['-datetime_modified']

    def get_metric_area(self):
        metric_area = self.unit_sqft * 0.0929

        return int(metric_area)

    def get_address(self):
        address = "{0}{1}{2}{3}".format(self.street, self.city, self.state, self.zip_code)

        return address

    def get_listings(self):
        listings = self.listings_set.all.order_by("-is_active", "-datetime_created")

        return listings
