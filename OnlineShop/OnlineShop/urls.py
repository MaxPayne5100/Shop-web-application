"""OnlineShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from account.views import sign_in_view, register_view, logout_view
from shop.views import shop_view, product_view, cart_screen_view, add_to_cart_view, remove_from_cart

from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    path('', include('main.urls')),
    path('admin/', admin.site.urls),
    path('about_us/', include('about_us.urls')),
    path('sign_in/', sign_in_view, name='sign_in'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('shop/', shop_view.as_view(), name='shop'),
    path('product/<slug>/', product_view.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart_view, name='add_to_cart'),
    path('shopping_cart/', cart_screen_view, name='shopping_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
