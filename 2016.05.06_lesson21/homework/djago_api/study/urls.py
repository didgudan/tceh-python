from django.conf.urls import url

from study.views import index, lessons, lesson, themes, theme

urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^lessons/$', lessons, name='lessons'),
    url(r'^lessons/(?P<lesson_pk>[0-9]+)/', lesson, name='lesson'),

    url(r'^themes/$', themes, name='themes'),
    url(r'^themes/(?P<theme_pk>[0-9]+)/', theme, name='theme'),
]
