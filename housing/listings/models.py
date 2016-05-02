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
    is_activated = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField()

    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=16)

    for_rent_by = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    lease_monthly_cost = models.CharField(max_length=255)
    lease_deposit = models.DecimalField(decimal_places=2, max_digits=10)
    lease_duration = models.CharField(max_length=255)
    lease_duration_custom = models.CharField(max_length=128)
    date_available = models.DateField()
    additional_lease_terms = models.TextField()
"""
- property_type (string)
- lease_whole_unit (boolean)
- owner_in_building (boolean)
- bedroom_count (string)
- bathroom_count (string)
- unit_sqft (string)
- unit_floor (string)
- furnished (string)
- furnished_details (string)

- is_water_included (boolean)
- is_electricity_included (boolean)
- is_heat_included (boolean)
- is_internet_included (boolean)
- is_cable_included (boolean)

- parking_space_count (integer)
- parking_type (string)
- pet_allowed (string)
- laundry_type (string)

- property_title (string)
- property_description (string) 

- has_dishwasher (boolean)
- has_garbage_disposal (bolean)
- has_microwave (boolean)
- has_fridge (boolean)
- laundry (string)
- cooling (string)

photo
"""
