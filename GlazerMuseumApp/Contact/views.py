from django.shortcuts import render

def contact_page(request):
    # Any context data you want to pass to the template can be defined here
    context = {
        'title': 'Contact Information',  # Example title for the page
        'content': 'This is the about page content.',  # Example content for the page
    }
    return render(request, 'Contact/contactpage.html', context)
