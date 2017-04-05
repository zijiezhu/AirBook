from django.conf.urls import url

from .lib import search
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search', search.search),
    url(r'^login', views.login),
    url(r'^signup', views.signup)
]
