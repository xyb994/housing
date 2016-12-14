from django import forms
from .models import Listing, HousingUser, Images

class HousingUserCreationForm(forms.ModelForm):
    class Meta:
        model = HousingUser
        fields = ("username", "password")

class ListingForm(forms.ModelForm):
    additional_lease_terms = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
        "placeholder": "Example: Owner pays for trash, sewer, and water. Owner "
        "shovel snow, lawn, garden, driveway maintenance."}))
    lease_duration_custom = forms.CharField(max_length=128, required=False,
        widget=forms.TextInput(attrs={"placeholder": "Other lease duration, example: 6/9 - 8/9/2016"}))
    date_available = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Listing
        exclude = (
        "listing_owner", "is_active", "datetime_modified", "datetime_created")
