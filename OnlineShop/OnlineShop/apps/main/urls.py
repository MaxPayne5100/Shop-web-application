from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_screen_view, name='main')
]