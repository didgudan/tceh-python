
from django.core.urlresolvers import reverse
from django.db.models import Avg, Count, F
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.utils import timezone

from pizza.models import PizzaOrder
from pizza.forms import PizzaOrderForm, DeliveryForm


# Create your views here.


def index(request):
    if request.method == 'GET':
        pizzas = PizzaOrder.objects.all()
        return render_to_response('pizza/index.html', {'pizzas': pizzas})
    return HttpResponse(status=405)


def create(request):
    if request.method == 'GET':
        c = RequestContext(request, {
            'pizza_form': PizzaOrderForm(),
            'delivery_form': DeliveryForm(),
        })
        return render_to_response('pizza/create.html', c)

    elif request.method == 'POST':
        pizza_form = PizzaOrderForm(request.POST)
        delivery_from = DeliveryForm(request.POST)
        if pizza_form.is_valid() and delivery_from.is_valid():
            delivery = delivery_from.save()
            pizza = pizza_form.save(delivery=delivery)
            pizza_form.save_m2m()

            return redirect(reverse('pizza:view', kwargs={
                'pizza_order_id': pizza.pk
            }))
        else:
            c = RequestContext(request, {
                'pizza_form': pizza_form,
                'delivery_form': delivery_from,
            })
            return render_to_response('pizza/create.html', c)
    return HttpResponse(status=405)


def view(request, pizza_order_id):
    if request.method == 'GET':
        # pizza = get_object_or_404(PizzaOrder, id=pizza_order_id)
        pizza = PizzaOrder.objects.get(id=pizza_order_id)
        return render_to_response('pizza/view.html', {'pizza': pizza})
    return HttpResponse(status=405)


def close(request, pizza_order_id):
    if request.method == 'GET':
        pizza = PizzaOrder.objects.get(id=pizza_order_id)
        pizza.mark_delivered()

        return redirect(reverse('pizza:view', kwargs={
            'pizza_order_id': pizza.pk
        }))
    return HttpResponse(status=405)


def stats(request):
    if request.method == 'GET':
        count = PizzaOrder.objects.count()
        average_extras = PizzaOrder.objects.all().annotate(
            extra_count=Count('extra')
        ).aggregate(result=Avg('extra_count'))

        today = timezone.now()
        query = {
            'date_created__day': today.day,
            'date_created__month': today.month,
            'date_created__year': today.year,
        }
        today_pizzas = PizzaOrder.objects.filter(
            **query
        ).count()

        today_delivered = PizzaOrder.objects.filter(
            delivered=True,  # TODO: manager
            **query
        ).count()

        # average_delivery_time = PizzaOrder.objects.filter(
        #     delivered=True,
        # ).annotate(
        #     diff=F('date_delivered') - F('date_created')
        # ).aggregate(result=Avg('diff'))

        params = {
            'count': count,
            'average_extras': average_extras['result'],
            'today_pizzas': today_pizzas,
            'today_delivered': today_delivered,
            # 'average_delivery_time': average_delivery_time,
        }

        return render_to_response('pizza/stats.html', {'params': params})
    return HttpResponse(status=405)
