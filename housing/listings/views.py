from django.shortcuts import redirect, render, render_to_response
from django.views import generic
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf

from .forms import ListingForm, HousingUserCreationForm
from .models import Listing

# index View
def index(request):
    listings = Listing.objects.filter(**get_queryset(request)).order_by(
        "-datetime_modified")

    # pagination
    paginator = Paginator(listings, 5) #listing per page
    page = request.GET.get("page")

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        listings = paginator.page(1)
    except EmptyPage:
        listings = paginator.page(1)

    # store queryset, pass for pagination
    queries_without_page = request.GET.copy()
    if "page" in queries_without_page:
        del queries_without_page["page"]

    return render(request, "listings/index.html",
        {"listings": listings, "queries_without_page": queries_without_page})


# get querysets using GET
def get_queryset(request):
    queryset = {"is_active": True}

    if request.GET.get("price"):
        queryset["lease_monthly_cost__gte"] = request.GET.get("price")

    if request.GET.get("type") in ["house", "apartment", "homestay"]:
        queryset["property_type"] = request.GET.get("type")

    if request.GET.get("beds"):
        queryset["bedroom_count__gte"] = request.GET.get("beds")

    return queryset


class ListingDetail(generic.DetailView):
    model = Listing
    template_name = "listings/detail.html"
    context_object_name = "listing"
    pk_url_kwarg = "listing_id"


# registration view
def register(request):
    if request.method == "POST":
        form = HousingUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.datetime_created = datetime.now()
            user.email = user.username
            user.set_password(request.POST.get("password"))
            form.save()
            return redirect("/accounts/register/complete")
    # if a GET (or any other method), create a blank form
    else:
        form = HousingUserCreationForm()
    token = {}
    token.update(csrf(request))
    token["form"] = form

    return render_to_response("accounts/registration_form.html", token)


class RegistrationCompleteView(generic.TemplateView):
    template_name = "accounts/registration_complete.html"


class ProfileView(generic.ListView):
    model = Listing
    template_name = "accounts/profile.html"
    context_object_name = "listings"

    # listings belong to the user
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProfileView, self).get_context_data(**kwargs)

        current_user = self.request.user
        context['listings'] = Listing.objects.filter(
            listing_owner=current_user).order_by(
            "-is_active", "-datetime_created")

        return context


class ListingCreate(generic.CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_edit.html"
    success_url = reverse_lazy("listings:profile")

    def form_valid(self, form):
        form.instance.listing_owner = self.request.user

        return super(ListingCreate, self).form_valid(form)


class ListingEdit(generic.UpdateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_edit.html"
    pk_url_kwarg = "listing_id"
    success_url = reverse_lazy("listings:profile")


def listing_status_toggle(request, listing_id):
        listing = Listing.objects.get(pk=listing_id)

        if listing.is_active:
            listing.is_active = False
        else:
            listing.is_active = True

        listing.save()

        return redirect("/accounts/profile")


# class IndexView(generic.list.ListView):
#     template = "listings/index.html"
#     context_object_name = "listings"
#     paginate_by = 5
#http://stackoverflow.com/questions/5907575/how-do-i-use-pagination-with-django-class-based-generic-listviews
#
#     def get_queryset(self):
#         queryset = {"is_active": True}
#
#         if (request.GET.get("price")):
#             queryset["lease_monthly_cost__gte"] = request.GET.get("price")
#
#         if (request.GET.get("type") in ["house", "apartment", "homestay"]):
#             queryset["property_type"] = request.GET.get("type")
#
#         if (request.GET.get("beds")):
#             queryset["bedroom_count__gte"] = request.GET.get("beds")
#
#         listings = Listing.objects.filter(**filter_querry).order_by(
#             "-datetime_modified")
#
#         return listings
