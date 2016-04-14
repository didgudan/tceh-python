from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import View
from django.contrib import messages

from my_app.forms import MyForm


def index(request):
    if request.method == "GET":
        return render_to_response('index.html', RequestContext(request))


class MyView(View):

    def get(self, request):
        form = MyForm()
        c = RequestContext(request, {'form': form})
        return render_to_response('form.html', c)

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'Validation failed')
        c = RequestContext(request, {'form': form})
        return render_to_response('form.html', c)