from django.contrib import admin
from django.urls import path
from app.views import show

urlpatterns = [
    path('login/', show),

]