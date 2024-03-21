from django.shortcuts import render
from .models import LoginText

def login_page(request):
    # Retrieve any necessary data from the database or perform any other logic
    login_data = LoginText.objects.all()
    
    # Render the login page template and pass any context data if needed
    return render(request, 'Login/loginpage.html', {'login_data': login_data})
