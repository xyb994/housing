from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import FilterForm

from .models import Listing

# Create your views here.
def index(request):
    queries_without_page = request.GET.copy()

    if "page" in queries_without_page:
        del queries_without_page["page"]

    filter_querry = {"is_active": True}

    if (request.GET.get("price")):
        filter_querry["lease_monthly_cost__gte"] = request.GET.get("price")

    if (request.GET.get("type") in ["house", "apartment", "homestay"]):
        filter_querry["property_type"] = request.GET.get("type")

    if (request.GET.get("beds")):
        filter_querry["bedroom_count__gte"] = request.GET.get("beds")

    listings = Listing.objects.filter(**filter_querry).order_by("-datetime_modified")

    paginator = Paginator(listings, 5) #listing per page
    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(1)

    return render(request, "listings/index.html", {"listings": listings, 'queries_without_page': queries_without_page})

def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "listings/detail.html", {"listing": listing})
