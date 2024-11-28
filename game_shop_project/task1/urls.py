from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.shop_view, name='products'),
    path('cart/', views.cart_view, name='cart'),
    path('shop/', views.shop_view, name='shop'),
    path('register/', views.register_view, name='register'),
]
