from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:SPText_id>/", views.details, name="details")
]