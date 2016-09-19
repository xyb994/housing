from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class HousingUser(AbstractUser):
    #USERNAME_FIELD = 'email'
    #first name = models.CharField(max_length=255) #django field builtin
    #last name = models.CharField(max_length=255) #django field builtin
    #is_admin = models.BooleanField(default=False) # django field builtin
    #email = models.EmailField(unique=True) # django field builtin
    #password = models.CharField() (encrypted string) #django field builtin
    phone = models.CharField(max_length=15)
    #is_avtive = models.BooleanField(default=False) #django field builtin
    #datetime_created = models.DateTimeField(auto_now_add=True)

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
        ('apartment', 'Apartment'),
        ('single_family_house', 'Single family house'),
        ('homestay', 'Homestay: live within house owner(share kitchen and/or bathroom)'),
    )

    FURNISHED_CHOICES = (
        ('unfurnished', 'Unfurnished'),
        ('lightly_furnished', 'Lightly furnished'),
        ('fully_furnished', 'Fully furnished'),
    )

    PARKING_SPACE_COUNT_CHOICES = (
        ('0', '0'),
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

    LAUNDRY_CHOICES = (
        ('none', 'None'),
        ('washer_and_dryer', 'Washer & Dryer'),
        ('washer', 'Washer'),
        ('dryer', 'Dryer'),
    )

    COOLING_CHOICES = (
        ('none', 'None'),
        ('air_conditioning', 'Air conditioning'),
        ('central_ac', 'Central A/C'),
    )

    is_active = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=9)
    for_rent_by = models.CharField(max_length=255, choices=FOR_RENT_BY_CHOICES)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    lease_monthly_cost = models.PositiveSmallIntegerField(default='')
    lease_deposit = models.PositiveSmallIntegerField(default='')
    lease_duration = models.CharField(max_length=255, choices=LEASE_DURATION_CHOICES)
    lease_duration_custom = models.CharField(max_length=128, blank=True, default='')
    date_available = models.DateField()
    additional_lease_terms = models.TextField(blank=True, help_text='Example: Owner pays for trash and sewer. Tenant responsible for gas and electric. Must have a minimum credit score of 640. Owner shovel snow, lawn, garden, driveway maintenance', default='')
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    lease_whole_unit = models.BooleanField(default=False)
    owner_in_building = models.BooleanField(default=False)
    bedroom_count = models.PositiveSmallIntegerField(default='')
    bathroom_count = models.PositiveSmallIntegerField(default='')
    unit_sqft = models.PositiveSmallIntegerField(blank=True, default='')
    unit_floor = models.PositiveSmallIntegerField(default='')
    furnished = models.CharField(max_length=11, choices=FURNISHED_CHOICES)
    furnished_details = models.TextField(blank=True, help_text='Example: bed only...', default='')
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
    laundry = models.CharField(max_length=15, choices=LAUNDRY_CHOICES)
    cooling = models.CharField(max_length=20, choices=COOLING_CHOICES)

    def get_name(self):
        name = self.first_name + self.last_name
        return name
#photo
'''
max_length?
smallIntegerField?
primary key?
'''
