from django import forms
from django.forms import ModelForm

from shop.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'image': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
        }
