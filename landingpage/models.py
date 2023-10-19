from django.db import models
import os

class ClientData(models.Model):
    name = models.CharField(max_length=100, verbose_name='Full Name')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    city = models.CharField(max_length=100, verbose_name='City')

    def __str__(self):
        return self.name

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/', verbose_name='Image')

    def __str__(self):
        return os.path.basename(str(self.image_file))

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
