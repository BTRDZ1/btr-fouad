from django.db import models
import os

class Image(models.Model):
    image_file = models.ImageField(upload_to='images/', verbose_name='Image')

    def __str__(self):
        return os.path.basename(str(self.image_file))

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
