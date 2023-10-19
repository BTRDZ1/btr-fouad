from django.db import models
from landingpage.models import Image  # Adjust this import to your project's structure


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product Name')
    images = models.ManyToManyField(Image, related_name='products')

    def __str__(self):
        return self.name
