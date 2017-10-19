from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='portfolio'),
    url(r'^projects/(?P<project_id>[\w-]+)/$', views.project, name='project'),
]
