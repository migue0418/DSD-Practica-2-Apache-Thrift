
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

urlpatterns = [
    url('', views.index),
]

urlpatterns += staticfiles_urlpatterns()
