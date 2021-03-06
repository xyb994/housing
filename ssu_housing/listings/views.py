# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

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


class ListingDetail(DetailView):
    model = Listing
    template_name = "listings/detail.html"
    context_object_name = "listing"
    pk_url_kwarg = "listing_id"

    def is_user_authorized(self, request):
        if not self.get_object().is_active:
            if request.user.is_authenticated():
                if self.get_object().listing_owner == HousingUser.objects.get(
                    id=self.request.user.pk):
                    return True
            return False
        return True

    def dispatch(self, request, *args, **kwargs):
        if not self.is_user_authorized(request):
            return HttpResponseForbidden()

        return super(ListingDetail, self).dispatch(request, *args, **kwargs)


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

    def is_user_authorized(self, request):
        if request.user.is_authenticated():
            self.object = self.get_object()
            return self.object.listing_owner == HousingUser.objects.get(
                id=self.request.user.pk)
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.is_user_authorized(request):
            return HttpResponseForbidden()
        else:
            return super(ListingEdit, self).dispatch(request, *args, **kwargs)


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
