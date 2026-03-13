from django.urls import path
from .views import salary, code

urlpatterns = [
    path('code', code),
    path('salary', salary),
]