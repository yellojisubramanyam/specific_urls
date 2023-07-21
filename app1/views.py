from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def first(request):
    return HttpResponse('Hi Goodmorning1')


def second(request):
    return HttpResponse('Good Afternoon2')
