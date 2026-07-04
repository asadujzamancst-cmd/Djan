from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse('welcome to home page')



def profile(request):
    return HttpResponse('welcome to profile page')


def dashboard(request):
    return HttpResponse('welcome to dashboard page')