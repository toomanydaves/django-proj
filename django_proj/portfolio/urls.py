from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/([\w-]+)/$', views.project, name='project'),
]
