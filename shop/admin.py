from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ['text', 'price', 'quantity', 'image']


admin.site.register(Product)
