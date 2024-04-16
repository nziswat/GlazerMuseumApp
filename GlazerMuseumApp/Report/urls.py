
from django.urls import path

from . import views
app_name = "report"
urlpatterns = [
    path("", views.report_page, name="report_page"),
    path("submit/", views.submit, name="submit")
]