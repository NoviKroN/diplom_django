from django.urls import path

from .views import ProductView

urlpatterns = [
    path("product/<int:id>", ProductView.as_view(), name="product-detail"),
]
