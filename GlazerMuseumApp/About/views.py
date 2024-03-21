from django.shortcuts import render

def about_page(request):
    # Any context data you want to pass to the template can be defined here
    context = {
        'title': 'About Us',  # Example title for the page
        'content': 'This is the about page content.',  # Example content for the page
    }
    return render(request, 'About/aboutpage.html', context)
