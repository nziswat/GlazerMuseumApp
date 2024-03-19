#exhibit page view
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from .models import ExText, PlayTypes

def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))

def details(request,ExText_id):
    exhibitText = ExText.objects.get(id=ExText_id)
    template = loader.get_template("ExhibitPage/details.html")
    context = {"ExText":exhibitText,"plays":exhibitText.exhibitPlays.play_set.all()}
   # plays= {"plays":}
    return HttpResponse(template.render(context,request)) #only takes two args, pass all to context

def vote(request, question_id):
    return HttpResponse(question_id)

def ExhibitPage(request):
    exhibitList = ExText.objects.all()
    context = {"exhibitList": exhibitList}
    return render(request, 'ExhibitPage/index.html', context)