from django.contrib import admin
from listings import models
# Register your models here.
admin.site.register(models.HousingUser)
admin.site.register(models.Listing)