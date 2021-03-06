from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = "folio"
urlpatterns = [
    path("", TemplateView.as_view(template_name="folio/index.html"), name="index"),
    path("projects/", views.ProjectListView.as_view(), name="projects"),
    path("projects/<slug:slug>/", views.ProjectDetailView.as_view(), name="detail"),
    path("tag/<slug:slug>/", views.TagDetailView.as_view(), name="tag_detail"),
]
