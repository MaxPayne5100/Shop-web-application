from django.shortcuts import render

# Create your views here.

def about_screen_view(request):
    return render(request, "about_us.html", {})