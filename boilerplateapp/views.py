from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Customer
from .serializers import CustomerSerializer


@api_view(["GET"])
def apiOverview(request):
    api_overview = {
        "Customer List": "/customer_list/",
        "Detail Customer View": "/customer_detail/<str:pk>/",
        "Create Customer": "/create_customer/",
        "Update Customer": "/update_customer/<str:pk>/",
    }
    return Response(api_overview)


@api_view(["GET"])
def customerList(request):
    customers = Customer.objects.all()
    serializer = CustomerSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def customerDetail(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def createCustomer(request):
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET", "POST"])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(data=request.data, instance=customer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteCustomer(request, pk):
    Customer.objects.get(id=pk).delete()
    return Response()
