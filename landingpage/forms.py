from django import forms
from .models import ClientData, Image

class ClientDataForm(forms.ModelForm):
    class Meta:
        model = ClientData
        fields = ['name', 'phone', 'city']
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'city': 'City',
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_file']
