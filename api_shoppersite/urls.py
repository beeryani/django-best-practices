from django.urls import path
from . import views

urlpatterns =[
    path('', views.getData),
    path('create_customer/', views.createCustomer),
]
