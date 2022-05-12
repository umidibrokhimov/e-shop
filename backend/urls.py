from django.urls import path, include
from .views import *

app_name='e-shop'

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('shop/', Shop.as_view(), name="shop"),
    path('detail/', ProductDetail.as_view(), name="product-detail"),
]