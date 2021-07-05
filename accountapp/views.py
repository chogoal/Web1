from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(requests):
    # return HttpResponse('Hello World!') # alt + enter 로 간단히 import
    return render(requests, 'accountapp/hello_world.html')