
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('', views.index),
]

urlpatterns += staticfiles_urlpatterns()