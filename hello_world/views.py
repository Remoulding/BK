# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. Your blueking app is running successfully now.")
    
def helloworld(request):
    return render(request, 'hello_world/helloworld.html')
