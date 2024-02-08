from django.http import HttpResponse
from django.template import loader

from django.urls import path

# Create your views here.
def index(request):

    return HttpResponse("Merely a test of the splash. Manually type your desired link for now")