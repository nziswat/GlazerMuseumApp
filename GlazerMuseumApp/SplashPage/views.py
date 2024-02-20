#exhibit page view
from django.http import HttpResponse
from django.template import loader

from .models import SPText

def index(request):
    Splashpage = SPText.objects.all()
    template = loader.get_template("SplashPage/SplashPage.html")
    context = {"Splashpage":Splashpage}

    return HttpResponse(template.render(context,request))

def details(request,SPText_id):
    SplashpageText = SPText.objects.get(id=SPText_id)
    template = loader.get_template("SplashPage/details.html")
    context = {"SPText":SplashpageText}

    return HttpResponse(template.render(context,request))