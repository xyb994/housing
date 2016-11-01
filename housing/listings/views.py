from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing

# Create your views here.
def index(request):
    active_listings = Listing.objects.filter(is_active=True)
    paginator = Paginator(active_listings, 5) #listing per page

    page = request.GET.get('page')
    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(1)

    return render(request, 'listings/index.html', {'listings': listings })

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "listings/detail.html", {"listing": listing})
