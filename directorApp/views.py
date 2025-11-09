from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexdirector(request):
    return HttpResponse("Welcome to the director Dashboard")