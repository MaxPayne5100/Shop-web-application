from django.urls import path

from . import views

urlpatterns = [
    path('', views.about_screen_view, name='about_us')
]