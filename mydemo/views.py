from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# food/views.py
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("<h1>Hello World!</h1>")
