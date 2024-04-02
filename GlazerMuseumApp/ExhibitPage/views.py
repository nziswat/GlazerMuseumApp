#This File was generated by Django and modified by: Kevin Panasiuk
#Log:
#4/1/24: Made this header.
#4/2/24: Added comments

from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from django.urls import reverse
from .models import ExText, PlayTypes, Play, Vote
from django.views.decorators.csrf import ensure_csrf_cookie



def index(request): #index is the base view, displays all the exhibits in a list.
    exhibitList = ExText.objects.all() 
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context, all the tempaltes work like this

@ensure_csrf_cookie #csrf_cookie used for user verification and 'security'
def details(request,ExText_id): #details is as it says, show the details for the exhibit.
    exhibitText = ExText.objects.get(pk=ExText_id)
    playset = exhibitText.get_play_types()
    template = loader.get_template("ExhibitPage/details.html")
    context = {"ExText":exhibitText,"plays":playset.all(),"exid":ExText_id}
    return HttpResponse(template.render(context,request)) 

def vote(request, ExText_id): #vote 'page' redirects straight back to previous page (should be details)
    unique_id = getattr(request, 'unique_id', None) #gets the unique ID generated for the user 
    exhibit = ExText.objects.get(id=ExText_id)
    plays = exhibit.get_play_types() #get the list of plays in the exhibit's play set     
    choices = request.POST.getlist('plays[]') #filter the plays by the plays selected with the vote
    selected_plays = plays.filter(playName__in=choices) 
    purgingVotes = Vote.objects.filter(cookie=unique_id, exhibit=exhibit) #get all votes that match the cookie and exhibit
    purgingVotes.delete() #just delete them

    for each in selected_plays:  #pick each play and add a vote by exhibit and cookie
        #Time stamp is handled by the vote creation itself
        each.addvote(exhibit,unique_id)
        each.save()


    referer_url = request.META.get('HTTP_REFERER') #get the previous page
    if referer_url: #go back to the previous page
        return HttpResponseRedirect(referer_url)
    else: #or return to the exhibits list by default, if this for some reason fails
        return HttpResponseRedirect(reverse('exhibits:index'))