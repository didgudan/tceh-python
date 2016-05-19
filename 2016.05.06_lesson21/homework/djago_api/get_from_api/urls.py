from django.conf.urls import url

from get_from_api.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    # url(r'^lessons/$', lessons, name='lessons'),
    # url(r'^themes/$', themes, name='themes'),
]
