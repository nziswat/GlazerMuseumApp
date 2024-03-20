#exhibit page view
from math import e
from django.http import HttpResponse
from django.template import loader
from django.db.models import F

from .models import ExText, PlayTypes

def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))
e
def details(request,ExText_id):
    exhibitText = ExText.objects.get(id=ExText_id)
    template = loader.get_template("ExhibitPage/details.html")
    context = {"ExText":exhibitText,"plays":exhibitText.exhibitPlays.play_set.all(),"exid":ExText_id}
   # plays= {"plays":}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context

def vote(request, ExText_id):
    exhibit = ExText.objects.get(id=ExText_id)
    plays = exhibit.exhibitPlays.play_set.all()
    
        
    #choices = plays.get(pk=request.POST["play"])
    choices = request.POST.getlist('plays[]')
    selected_plays = plays.filter(pk__in=choices)


    for each in selected_plays:
        each.addvote()
        each.save()

    return HttpResponse(request)
    
    

#def vote(request, question_id):
#    return HttpResponse(question_id)
