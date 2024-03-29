from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name='e-shop'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('products/', Shop.as_view(), name="shop"),
    path('products/<int:pk>/', ProductDetail.as_view(), name="product-detail"),
    path('cart/', ShoppingCart.as_view(), name="cart"),
    path('contact/', Contact.as_view(), name="contact"),
    path('checkout/', Checkout.as_view(), name="checkout"),
    path('profile/', profile, name='user-profile'),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', SignUpView.as_view(), name="registraion"),
]