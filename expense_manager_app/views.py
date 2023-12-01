from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the expense manager")
