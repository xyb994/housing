from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    furnished_details = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Example: bed and desk only"}))
    additional_lease_terms = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'class': 'form-control',
        "placeholder": "Example: Owner pays for trash, sewer, and water. Owner "
        "shovel snow, lawn, garden, driveway maintenance."}))
    lease_duration_custom = forms.CharField(max_length=128, required=False,
        widget=forms.TextInput(attrs={"placeholder": "Example: 6/9 - 8/9/2016"}))
    date_available = forms.DateField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Listing
        exclude = ("listing_owner", "is_active", "datetime_modified",
            "datetime_created")