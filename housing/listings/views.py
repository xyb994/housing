from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from datetime import datetime

from .forms import ListingForm, HousingUserCreationForm
from .models import Listing

# index homepage view
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

    listings = Listing.objects.filter(**filter_querry).order_by(
        "-datetime_modified")

    paginator = Paginator(listings, 5) #listing per page
    page = request.GET.get("page")

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(1)

    return render(request, "listings/index.html", {"listings": listings,
        "queries_without_page": queries_without_page,
        "filter_querry": filter_querry})

# listing detail view
def detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "listings/detail.html", {"listing": listing})

# registration view
def register(request):
    if request.method == "POST":
        form = HousingUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.datetime_created = datetime.now()
            user.email = user.username
            user.set_password(request.POST.get("password"))
            user.save()
            return HttpResponseRedirect("/accounts/register/complete")
    # if a GET (or any other method), create a blank form
    else:
        form = HousingUserCreationForm()
    token = {}
    token.update(csrf(request))
    token["form"] = form

    return render_to_response("registration/registration_form.html", token)

# registration complete view
def registration_complete(request):
    return render_to_response("registration/registration_complete.html")

# account profile view
@login_required
def profile(request):
    if request.method == "POST":
        listing_id = request.POST.get("listing-to-be-changed")
        print("listing id:")
        print(listing_id)
        listing = Listing.objects.get(pk=listing_id)

        if (listing.is_active):
            listing.is_active = False
        else:
            listing.is_active = True

        listing.save()

    listings = Listing.objects.filter(listing_owner=request.user).order_by(
        "-is_active", "-datetime_created")
    return render(request, "accounts/profile.html", {"listings": listings})

# Create new listing view
@login_required
def newListing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.datetime_modified = datetime.now()
            listing.listing_owner = request.user
            listing.save()
            return redirect("/accounts/profile")
    # if a GET (or any other method), create a blank form
    else:
        form = ListingForm()

    return render(request, "listings/listing_edit.html", {"form": form})

# Edit Listing Detail View
def editListing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == "POST":
        form = ListingForm(request.POST, instance=post)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = request.user
            listing.published_date = timezone.now()
            listing.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ListingForm(instance=post)
    return render(request, 'listings/listing_edit.html', {'form': form})
