from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendemail(request):
    return HttpResponse("sendemail")
