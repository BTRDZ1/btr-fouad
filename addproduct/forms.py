from django import forms
from .models import Product
from landingpage.models import Image  # Adjust this import to your project's structure

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'images']  # Include 'images' field

    images = forms.ModelMultipleChoiceField(
        queryset=Image.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
