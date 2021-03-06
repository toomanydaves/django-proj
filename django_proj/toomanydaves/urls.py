"""toomanydaves URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from toomanydaves import views
from toomanydaves_auth import views as toomanydaves_auth_views
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as contrib_auth_views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^backstory/$', views.backstory, name='backstory'),
    url(r'^poem/$', views.poem, name='poem'),
    url(r'^engage/$', views.engage, name='engage'),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^network/', include('network.urls')),
    url(r'^people/$', toomanydaves_auth_views.people, name="people"),
    url(r'^people/(?P<user_id>[\w-]+)/$', toomanydaves_auth_views.person, name="person"),
    url(r'^login/$', contrib_auth_views.login, name='login'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^admin/logout/$', views.logout_user, name='logout_admin'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
