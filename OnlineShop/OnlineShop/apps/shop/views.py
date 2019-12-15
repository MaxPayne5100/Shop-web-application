from django.shortcuts import render

from .models import Product

# Create your views here.

def products_view(request):
    context = {}
    context["products"] = Product.objects.all()
    return render(request, 'shop.html', context)