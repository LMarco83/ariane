from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
     path('rate/<int:rating>/', views.rate),
     path('', views.index, name="index"),

]
