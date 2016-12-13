from django.conf.urls import url

from . import views

app_name = 'listings'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<listing_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
    url(r'^newListing$', views.newListing, name='newListing'),
]
