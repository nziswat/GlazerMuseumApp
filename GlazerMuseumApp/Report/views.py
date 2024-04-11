from django.shortcuts import render

def report_page(request):
    # Any context data you want to pass to the template can be defined here
    context = {
        'title': 'Report Information',  # Example title for the page
        'content': 'This is the about page content.',  # Example content for the page
    }
    return render(request, 'Report/reportpage.html', context)
