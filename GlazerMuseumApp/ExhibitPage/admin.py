from django.contrib import admin

from .models import ExText, Play, PlayTypes

admin.site.register(ExText)
admin.site.register(Play)
admin.site.register(PlayTypes)