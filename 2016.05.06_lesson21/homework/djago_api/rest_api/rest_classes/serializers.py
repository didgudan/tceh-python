# -*- coding: utf-8 -*-

from rest_framework import serializers

from study.models import Lesson, Theme


class ThemeSerializer(serializers.HyperlinkedModelSerializer):
    lesson = serializers.StringRelatedField(many=False)

    class Meta:
        model = Theme
        fields = ('name', 'description', 'lesson')


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    theme = serializers.StringRelatedField(many=True)

    class Meta:
        model = Lesson
        fields = ('number', 'title', 'theme')
