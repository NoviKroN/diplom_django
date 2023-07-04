from django.urls import path

from .views import ProductView, ProductReviewView

urlpatterns = [
    path("product/<int:id>", ProductView.as_view(), name="product-detail"),
    path('product/<int:id>/review', ProductReviewView.as_view(), name='post_product_review'),
]
