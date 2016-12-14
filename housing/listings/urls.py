from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views

from . import views

app_name="listings"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.RegistrationCompleteView.as_view(), name='registration_complete'),
    url(r'^accounts/profile/$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^listing/new/$', login_required(views.ListingCreate.as_view()), name='new'),
    url(r'^listing/(?P<listing_id>\d+)/$', views.ListingDetail.as_view(), name='detail'),
    url(r'^listing/(?P<listing_id>\d+)/edit/$', login_required(views.ListingEdit.as_view()), name='edit'),
    url(r'^listing/(?P<listing_id>\d+)/toggle/$', login_required(views.listing_status_toggle), name='toggle'),
]
