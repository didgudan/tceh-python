from django.shortcuts import render
from django.db import transaction
from django.http import Http404

from study.forms import LessonForm, ThemeForm
from study.models import Lesson, Theme

import pdb

def index(request):
    return render(request, 'study/index.html')


def lessons(request):
    lesson_form = LessonForm(
        initial={'number': Lesson.objects.last().number + 1}
    )

    if request.method == 'POST':
        previous_lesson_form = LessonForm(request.POST)
        if previous_lesson_form.is_valid():
            with transaction.atomic():
                previous_lesson_form.save()
            lesson_form.initial['number'] += 1
        else:
            lesson_form = previous_lesson_form

    return render(request, 'study/lessons.html', {
        'lessons': Lesson.objects.all(),
        'form': lesson_form,
    })


def lesson(request, lesson_pk):
    try:
        lesson_form = LessonForm(instance=Lesson.objects.get(pk=lesson_pk))
    except Lesson.DoesNotExist:
        raise Http404('There in no such lesson!')

    if request.method == 'POST':
        instance = Lesson.objects.get(pk=lesson_pk)
        previous_lesson_form = LessonForm(request.POST, instance=instance)
        if previous_lesson_form.is_valid():
            with transaction.atomic():
                previous_lesson_form.save()
            lesson_form = previous_lesson_form

    return render(request, 'study/lesson.html', {
        'form': lesson_form,
        'themes': Lesson.objects.get(pk=lesson_pk).theme.all(),
    })


def themes(request):
    theme_form = ThemeForm()

    if request.method == 'POST':
        previous_theme_form = ThemeForm(request.POST)
        if previous_theme_form.is_valid():
            with transaction.atomic():
                previous_theme_form.save()
        else:
            theme_form = previous_theme_form

    return render(request, 'study/themes.html', {
        'themes': Theme.objects.all(),
        'form': theme_form,
    })


def theme(request, theme_pk):
    try:
        theme_form = ThemeForm(instance=Theme.objects.get(pk=theme_pk))
    except Theme.DoesNotExist:
        raise Http404('There in no such lesson theme!')

    if request.method == 'POST':
        instance = Theme.objects.get(pk=theme_pk)
        previous_theme_form = ThemeForm(request.POST, instance=instance)
        if previous_theme_form.is_valid():
            with transaction.atomic():
                previous_theme_form.save()
            theme_form = previous_theme_form

    return render(request, 'study/theme.html', {
        'form': theme_form,
    })
