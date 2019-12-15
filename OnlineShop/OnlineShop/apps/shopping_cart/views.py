from django.shortcuts import render

# Create your views here.

def cart_screen_view(request):
    return render(request, "shopping_cart.html", {})