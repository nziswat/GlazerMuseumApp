from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:ExText_id>/", views.details, name="details")
]