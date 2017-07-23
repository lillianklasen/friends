from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^register$', views.register),
    url(r'^add-friend/(?P<id>\d+)$', views.addFriend),
    url(r'^remove-friend/(?P<id>\d+)$', views.removeFriend)
]
