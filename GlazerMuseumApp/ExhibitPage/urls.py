from django.urls import path

from . import views
app_name = "ExhibitPage"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:ExText_id>/", views.details, name="details"),
    path("<int:ExText_id>/vote/", views.vote, name="vote")
]