"""githubstars URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.views import login
from django.contrib.auth.views import logout

from githubstars.core.views import home
from githubstars.core.views import register
from githubstars.core.views import repositories


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': settings.LOGIN_URL}, name='logout'),
    url(r'^register/$', register, name='register'),
    url(r'^repositories/$', repositories, name='repositories'),
    url(r'^admin/', admin.site.urls),
]
