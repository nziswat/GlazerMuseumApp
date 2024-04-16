from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.urls import reverse
from .models import BugReport
from django.views.decorators.csrf import ensure_csrf_cookie

def addvote(self,exhibit,cookie): 
        newvote= Vote.objects.create(cookie=cookie,exhibit=exhibit,play=self) 

@ensure_csrf_cookie #csrf_cookie used for user verification and 'security'
def report_page(request):
    # Any context data you want to pass to the template can be defined here
    context = {
        'title': 'Report Information',  # Example title for the page
        'content': 'This is the about page content.',  # Example content for the page
    }
    return render(request, 'Report/reportpage.html', context)


def submit(request): 
    
    #shortDesc = request.POST.

    newBug = BugReport()




    referer_url = request.META.get('HTTP_REFERER') #get the previous page
    if referer_url: #go back to the previous page
        return HttpResponseRedirect(referer_url)
    else: #or return to the exhibits list by default, if this for some reason fails
        return HttpResponseRedirect(reverse('exhibits:index'))
