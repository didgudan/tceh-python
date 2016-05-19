from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from rest_api.rest_classes.views import LessonViewSet, ThemeViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'lesson', LessonViewSet, 'lesson-list')
router.register(r'theme', ThemeViewSet, 'theme-detail')

urlpatterns = router.urls
