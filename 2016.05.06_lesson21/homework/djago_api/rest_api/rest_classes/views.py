# -*- coding: utf-8 -*-

from rest_framework import viewsets

from study.models import Lesson, Theme
from rest_api.rest_classes.serializers import LessonSerializer, ThemeSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
