from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def goodbye(request):
    return HttpResponse("Good Bye")


def time(request):
    current_time = datetime.now().strftime("%H:%M:%S")
    return HttpResponse(current_time)


def home_page(request):
    return HttpResponse("Главная страница")

def about(request):
    return HttpResponse("О нас")