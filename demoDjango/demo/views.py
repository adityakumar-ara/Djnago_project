from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def overview(request):
   return HttpResponse("Hello Django")

def aditya(request):
   return HttpResponse("Hello Aditya!")