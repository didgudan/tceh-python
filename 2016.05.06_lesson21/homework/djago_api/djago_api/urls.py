"""djago_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from study import urls as study_urls
from rest_api import urls as rest_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/', include(rest_urls, namespace="rest_api")),
    url(r'^', include(study_urls, namespace='study')),
]


