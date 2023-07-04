from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, ProductReview


class ProductView(APIView):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            serialized_product = {
                "id": product.id,
                "category": product.category,
                "price": str(product.price),
                "count": product.count,
                "date": str(product.date),
                "title": product.title,
                "description": product.description,
                "fullDescription": product.fullDescription,
                "freeDelivery": product.freeDelivery,
                "images": [
                    {
                        "src": image.src.url,
                        "alt": image.alt
                    }
                    for image in product.images.all()
                ],
                "tags": [tag.name for tag in product.tags.all()],
                "reviews": [
                    {
                        "author": review.author,
                        "email": review.email,
                        "text": review.text,
                        "rate": review.rate,
                        "date": str(review.date)
                    }
                    for review in product.reviews.all()
                ],
                "specifications": [
                    {
                        "name": spec.name,
                        "value": spec.value
                    }
                    for spec in product.specifications.all()
                ],
                "rating": product.rating
            }
            return Response(serialized_product, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ProductReviewView(APIView):
    def post(self, request, id):
        author = request.data.get('author')
        email = request.data.get('email')
        text = request.data.get('text')
        rate = request.data.get('rate')
        date = request.data.get('date')

        review = ProductReview.objects.create(
            product_id=id,
            author=author,
            email=email,
            text=text,
            rate=rate,
            date=date
        )

        # You can perform any additional actions here if needed

        # Return the created review in the response
        response_data = {
            'author': review.author,
            'email': review.email,
            'text': review.text,
            'rate': review.rate,
            'date': review.date,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
