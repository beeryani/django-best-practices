from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Customer


def index(request):
    customer_list = Customer.objects.order_by('-id')
    context = {
        'customer_list': customer_list,
    }
    return render(request, 'shoppersite/index.html', context)
