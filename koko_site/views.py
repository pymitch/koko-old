from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return HttpResponse("Hello, World. This is the Homepage. Take a test or sign in")

def logout(request):
    logout(request)

def password_reset(request):
     password_reset(request)

# def password_change(request):
#     password_change(request)