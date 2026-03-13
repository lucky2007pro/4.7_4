from django.urls import path
from .views import vazifa, salary

urlpatterns = [
    path('vazifasi', vazifa),
    path('salary', salary),
]