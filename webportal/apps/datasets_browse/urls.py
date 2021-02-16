from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^datasetlist', views.datasets_browses_list, name='datasets_browses_list'),
]