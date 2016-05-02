from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

import pdb

from auth_app.forms import RegisterForm


def register(request):
    form = RegisterForm(request.POST or None)

    c = RequestContext(request, {
        'form': form,
    })

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            # pdb.set_trace()
            register_form.save()
            messages.success(
                request,
                'User %s was created successful!' % request.POST['username'],
            )

            return redirect(reverse('auth_app:register'))

    return render_to_response('auth_app/register.html', c)
