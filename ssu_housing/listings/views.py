# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

# from django.core.urlresolvers import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect, render, render_to_response
from django.views.generic import DetailView, TemplateView, ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context_processors import csrf

from .models import Listing, HousingUser, User
from .forms import ListingForm, HousingUserCreationForm


# index View
def index(request):
    listings = Listing.objects.filter(**get_queryset(request)).order_by(
        "-datetime_modified")

    # pagination
    paginator = Paginator(listings, 2) #listing per page
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


class ListingDetail(LoginRequiredMixin, DetailView):
    model = Listing
    template_name = "listings/detail.html"
    context_object_name = "listing"
    pk_url_kwarg = "listing_id"

    def dispatch(self, request, *args, **kwargs):
        #if inactive and user doesn't own it return forbidden
        #TODO: Refactor this to traverse request.user.housing_user

        if not self.get_object().is_active and self.get_object().listing_owner \
            != HousingUser.objects.filter(user=request.user).exists():
            return HttpResponseForbidden()

        return super(ListingDetail, self).dispatch(request, *args, **kwargs)

# registration view
def register(request):
    if request.method == "POST":
        form = HousingUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
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


class RegistrationCompleteView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/registration_complete.html"


class ProfileView(LoginRequiredMixin, ListView):
    model = HousingUser
    template_name = "accounts/profile.html"
    context_object_name = "listings"

    # listings belong to the user
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProfileView, self).get_context_data(**kwargs)

        current_user = self.request.user
        context['listings'] = Listing.objects.filter(
            listing_owner=HousingUser.objects.get(id=self.request.user.pk)).order_by(
            "-is_active", "-datetime_created")

        return context


class PreferenceView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/preference.html"


class ListingCreate(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_edit.html"
    success_url = reverse_lazy("listings:profile")

    def form_valid(self, form):
        form.instance.listing_owner = HousingUser.objects.get(
            id=self.request.user.pk)

        return super(ListingCreate, self).form_valid(form)


class ListingEdit(LoginRequiredMixin, UpdateView):
    model = Listing
    form_class = ListingForm
    template_name = "listings/listing_edit.html"
    pk_url_kwarg = "listing_id"
    success_url = reverse_lazy("listings:profile")

    def user_passes_test(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.listing_owner == HousingUser.objects.get(
                id=self.request.user.pk)
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return HttpResponseForbidden()
        else:
            return super(ListingEdit, self).dispatch(request, *args, **kwargs)
    # def get_queryset(self):
    #     base_qs = super(ListingEdit, self).get_queryset()
    #
    #     return base_qs.filter(listing_owner=self.request.user.pk)


def listing_status_toggle(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404
    else:
        if listing.listing_owner.pk == request.user.pk:
            if listing.is_active:
                listing.is_active = False
            else:
                listing.is_active = True

            listing.save()

            return redirect("/accounts/profile")
        else:
            return HttpResponseForbidden()
