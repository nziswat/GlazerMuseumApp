#exhibit page view
from django.http import HttpResponse
from django.template import loader
from django.db.models import F

from .models import ExText, PlayTypes, Play, Vote

def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))

def details(request,ExText_id):
    

    exhibitText = ExText.objects.get(pk=ExText_id)
    playset = exhibitText.get_play_types()
    template = loader.get_template("ExhibitPage/details.html")

    context = {"ExText":exhibitText,"plays":playset.all(),"exid":ExText_id}
   # plays= {"plays":}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context

def vote(request, ExText_id):
    exhibit = ExText.objects.get(id=ExText_id)
    plays = exhibit.get_play_types() #get the list of plays in the exhibit's play set     
    choices = request.POST.getlist('plays[]') #filter the plays by the plays selected with the vote
    selected_plays = plays.filter(playName__in=choices) #


    for each in selected_plays:  #pick each play and add a vote by exhibit and cookie
        #Time stamp is handled by the vote creation itself
        each.addvote(exhibit,'123debug123')
        each.save()

    return HttpResponse(selected_plays)
    
    
