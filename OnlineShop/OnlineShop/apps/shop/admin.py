from django.contrib import admin

# Register your models here.

from .models import Product, Order, ProductOrderTable

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrderTable)