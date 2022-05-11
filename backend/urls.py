from django.urls import path, include
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="Home"),
]