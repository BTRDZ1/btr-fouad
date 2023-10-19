import os
from django.db import models

class Image(models.Model):
    # Define the fields for the Image model here
    image_file = models.ImageField(upload_to='images/', verbose_name='Image')

    def __str__(self):
        return os.path.basename(str(self.image_file))

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
