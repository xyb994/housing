from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Listing

# Create your views here.
def index(request):
    latest_listings = Listing.objects.order_by('-datetime_modified')[:10]
    context = {'latest_listings': latest_listings}
    return render(request, 'listings/index.html', context)

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'listings/detail.html', {'listing': listing})
