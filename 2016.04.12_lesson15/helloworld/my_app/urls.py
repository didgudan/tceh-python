from django.conf.urls import url

from views import index, MyView

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^form/', MyView.as_view(), name='form'),
]
