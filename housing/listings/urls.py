from django.conf.urls import url

from . import views

app_name = 'listings'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<listing_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^newListing$', views.newListing, name='newListing'),
<<<<<<< Updated upstream
=======
    url(r'^accounts/', include('nopassword.urls', namespace='nopassword')),
>>>>>>> Stashed changes
]
