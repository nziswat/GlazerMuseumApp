from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the admin page
            return redirect(reverse('admin:index'))
        else:
            # Authentication failed
            # Handle it accordingly
            return render(request, 'Login/loginpage.html', {'error_message': 'Invalid credentials'})
        
        
    return render(request, 'Login/loginpage.html')
