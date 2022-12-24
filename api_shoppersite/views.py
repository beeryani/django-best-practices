from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from shoppersite.models import Customer
from .serializers import CustomerSerializer

@api_view(['GET'])
def getData(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many = True)
    return Response(serializer.data)
