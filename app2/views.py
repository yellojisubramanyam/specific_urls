from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('Hi Goodmorning3')


def second(request):
    return HttpResponse('Good Afternoon4')