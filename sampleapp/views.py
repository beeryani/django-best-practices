from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer


@api_view(["GET"])
def apiOverview(request):
    api_overview = {
        "Customer List": "/customer_list/",
        "Detail Customer View": "/customer_detail/<str:pk>/",
        "Create Customer": "/create_customer/",
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


class CreateCustomer(CreateAPIView):
    queryset = Customer.objects.all()
    serializer = CustomerSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        return CustomerSerializer
