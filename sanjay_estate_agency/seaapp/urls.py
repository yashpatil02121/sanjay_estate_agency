from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("buy", views.buy, name="buy"),
    path("rent", views.rent, name="rent"),
    path("sell", views.sell, name="sell"),
]

