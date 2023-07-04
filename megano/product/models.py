from django.db import models


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    fullDescription = models.TextField()
    freeDelivery = models.BooleanField()
    rating = models.FloatField()


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    src = models.ImageField(upload_to='product_images/')
    alt = models.CharField(max_length=255)


class ProductTag(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='tags')
    name = models.CharField(max_length=255)


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    rate = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'Product Review'
        verbose_name_plural = 'Product Reviews'


class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications')
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)


