from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview),
    path("customer_list/", views.customerList),
    path("customer_detail/<str:pk>/", views.customerDetail),
    path("create_customer/", views.createCustomer),
    path("update_customer/<str:pk>/", views.updateCustomer),
    path("delete_customer/<str:pk>/", views.deleteCustomer),
]
