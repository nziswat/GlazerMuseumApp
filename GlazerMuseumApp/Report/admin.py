from django.contrib import admin

# Register your models here.
from .models import BugReport

admin.site.register(BugReport)