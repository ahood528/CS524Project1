from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    template = loader.get_template('mainpage/index.html')
    context = {} # dictionary of variables
    return HttpResponse(template.render(context, request))

 
def caregiver(request):
    template = loader.get_template('mainpage/caregiver.html')
    context = {} # dictionary of variables
    return HttpResponse(template.render(context, request))