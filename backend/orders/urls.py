from django.urls import path

from .views import CheckoutView, OrderList

urlpatterns = [
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("", OrderList.as_view(), name="order-list"),
]
