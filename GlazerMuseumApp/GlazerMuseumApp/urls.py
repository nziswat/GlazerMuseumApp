"""
URL configuration for GlazerMuseumApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Login import views as login_views 
from About import views as about_views 
from Contact import views as contact_views
from Report import views as report_views
from django.conf.urls.static import static
from django.conf import settings

# 2FA
from django.contrib.auth.models import User  # Django default user model
from django_otp.admin import OTPAdminSite
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_totp.admin import TOTPDeviceAdmin

class OTPAdmin(OTPAdminSite):
    pass

# Register models from OTP package
admin_site = OTPAdmin(name='OTPAdmin')
admin_site.register(User)
admin_site.register(TOTPDevice, TOTPDeviceAdmin)

urlpatterns = [
    # URL pattern for the ExhibitPage app
    path('ExhibitPage/', include("ExhibitPage.urls", namespace='ExhibitPage')),

    # URL pattern for the login page
    path('GlazerStaff/', login_views.login_page, name='login_page'),  # Updated name to 'login_page'
    
    # URL pattern for the about page
    path('about/', about_views.about_page, name='about_page'),  

    # URL pattern for the contact page
    path('contact/', contact_views.contact_page, name='contact_page'),  

    # URL pattern for the Django admin page
    path('admin/', admin.site.urls, name='admin'),

    # URL pattern for the Report page
    path('report/', include("Report.urls", namespace='report')), 

    # URL pattern for the SplashPage app
    path('', include(("SplashPage.urls", 'SplashPage'), namespace='SplashPage')),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

