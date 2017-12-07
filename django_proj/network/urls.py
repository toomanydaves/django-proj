from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='network'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
]
