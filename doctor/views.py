from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def salary(request):
    return HttpResponse("Oylik maosh 200$.")

def vazifa(request):
    return HttpResponse("Shifokor odamlarni davolaydi.")