from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mendaftar.models import*
from . import views


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Event.objects.all(),template_name="Daftar/event.html")),
    url(r'^(?P<pk>\d+)$', ListView.as_view(model=Event, template_name='Daftar/from.html'))
    ]
