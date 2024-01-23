from django.http import HttpResponse

from .models import ExText

def index(request):
    output = ExText.titleText
    return HttpResponse(output)