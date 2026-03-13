from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def salary(request):
    return HttpResponse("Oylik maosh 500$.")
def code(request):
    return HttpResponse("Yozilgan kod uzunligi 500 qator.")