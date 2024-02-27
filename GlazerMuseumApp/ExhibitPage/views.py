#exhibit page view
from django.http import HttpResponse
from django.template import loader

from .models import ExText

def index(request):
    exhibitList = ExText.objects.all()
    template = loader.get_template("ExhibitPage/index.html")
    context = {"exhibitList":exhibitList}

    return HttpResponse(template.render(context,request))

def details(request,ExText_id):
    ExhibitText = ExText.objects.get(id=ExText_id)
    template = loader.get_template("ExhibitPage/details.html")
    context = {"ExText":ExhibitText}

    return HttpResponse(template.render(context,request))


