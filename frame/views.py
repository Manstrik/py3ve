from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Frame is a part of the window')
# Create your views here.