from django.urls import path, include
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

app_name='e-shop'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('shop/', Shop.as_view(), name="shop"),
    path('detail/', ProductDetail.as_view(), name="product-detail"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]