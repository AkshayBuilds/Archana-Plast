"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.urls import re_path

from django.urls import re_path

urlpatterns = [
    path('', home, name="home"),
    path('index/', home, name="home2"),
    path('admin/', admin.site.urls),
    path('about.html', about, name="about"),
    re_path(r'^service/?$', service, name="service"),
    re_path(r'^contact/?$', contact, name="contact"),
    re_path(r'^project/?$', project, name="project"),
    re_path(r'^saveEnquiry/?$', saveEnquiry, name="saveEnquiry"),
]
