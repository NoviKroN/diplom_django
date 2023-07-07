from django.urls import path
from cart.views import CartDetailView

urlpatterns = [
    path('basket', CartDetailView.as_view(), name='cart-detail'),
]
