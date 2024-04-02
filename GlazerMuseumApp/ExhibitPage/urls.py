#This File was generated by Django and modified by: Kevin Panasiuk
#Log:
#4/1/24: Made this header.

from django.urls import path

from . import views
app_name = "ExhibitPage"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:ExhibitData_id>/", views.details, name="details"),
    path("<int:ExhibitData_id>/vote/", views.vote, name="vote")
]