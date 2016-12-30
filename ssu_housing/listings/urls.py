# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name="listings"

urlpatterns = [
    url(
        regex=r'^$',
        view=views.index,
        name='index'
    ),
    url(
        regex=r'^listing/new/$',
        view=login_required(views.ListingCreate.as_view()),
        name='new'
    ),
    url(
        regex=r'^listing/(?P<listing_id>\d+)/$',
        view=views.ListingDetail.as_view(),
        name='detail'
    ),
    url(
        regex=r'^listing/(?P<listing_id>\d+)/edit/$',
        view=login_required(views.ListingEdit.as_view()),
        name='edit'
    ),
    url(
        regex=r'^listing/(?P<listing_id>\d+)/toggle/$',
        view=login_required(views.listing_status_toggle),
        name='toggle'
    ),
    url(
        regex=r'^accounts/profile/$',
        view=login_required(views.ProfileView.as_view()),
        name='profile'
    ),
    url(
        regex=r'^accounts/profile/preference$',
        view=login_required(views.PreferenceView.as_view()),
        name='preference'
    ),
]
