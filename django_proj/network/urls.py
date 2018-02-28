from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='network'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^peeps/(?P<peep_id>[\w-]+)/$', views.peep, name="peep"),
    url(r'^peeps/$', views.peeps, name="peeps"),
]
