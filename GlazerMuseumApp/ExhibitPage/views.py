#exhibit page view
from django.http import HttpResponse
from django.template import loader
from django.db.models import F

from .models import ExText, PlayTypes

def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))

def details(request,ExText_id):
    exhibitText = ExText.objects.get(id=ExText_id)
    template = loader.get_template("ExhibitPage/details.html")
    context = {"ExText":exhibitText,"plays":exhibitText.exhibitPlays.play_set.all(),"exid":ExText_id}
   # plays= {"plays":}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context

def vote(request, ExText_id):
    exhibit = ExText.objects.get(id=ExText_id)
    plays = exhibit.exhibitPlays.play_set.all()
        
    choices = plays.get(pk=request.POST["play"])

    for each in choices:
        each.votes = F("votes") + 1
        each.save()
    return HttpResponse(request)
    
    

#def vote(request, question_id):
#    return HttpResponse(question_id)