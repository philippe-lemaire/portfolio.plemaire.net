from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "folio"
urlpatterns = [
    path("", TemplateView.as_view(template_name="folio/index.html"), name="index"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
]
