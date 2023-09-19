import imp
from django.urls import path
from .views import makeOrder

urlpatterns = [
    path('order/', makeOrder, name="checkout.order")
]
