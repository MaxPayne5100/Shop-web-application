from django.contrib import admin

# Register your models here.

from .models import Product, Order, ProductOrderTable, Review

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrderTable)
admin.site.register(Review)