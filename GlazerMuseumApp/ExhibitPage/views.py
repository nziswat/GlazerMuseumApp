#exhibit page view
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import ExText, PlayTypes, Play, Vote
from django.views.decorators.csrf import ensure_csrf_cookie



def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))

@ensure_csrf_cookie
def details(request,ExText_id):
    

    exhibitText = ExText.objects.get(pk=ExText_id)
    playset = exhibitText.get_play_types()
    template = loader.get_template("ExhibitPage/details.html")

    context = {"ExText":exhibitText,"plays":playset.all(),"exid":ExText_id}
   # plays= {"plays":}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context

def vote(request, ExText_id): #TODO: redirect back to exhibits, maybe give a thank you or something
    unique_id = getattr(request, 'unique_id', None) #gets the unique ID generated for the user 
    exhibit = ExText.objects.get(id=ExText_id)
    plays = exhibit.get_play_types() #get the list of plays in the exhibit's play set     
    choices = request.POST.getlist('plays[]') #filter the plays by the plays selected with the vote
    selected_plays = plays.filter(playName__in=choices) #
    purgingVotes = Vote.objects.filter(cookie=unique_id, exhibit=exhibit) #get all votes that match the cookie and exhibit
    purgingVotes.delete() #just delete them

    for each in selected_plays:  #pick each play and add a vote by exhibit and cookie
        #Time stamp is handled by the vote creation itself
        each.addvote(exhibit,unique_id)
        each.save()


    referer_url = request.META.get('HTTP_REFERER')
    if referer_url: #go back to the previous page
        return HttpResponseRedirect(referer_url)
    else: #or return to the exhibits list by default, if this for some reason fails
        return HttpResponseRedirect(reverse('exhibits:index'))