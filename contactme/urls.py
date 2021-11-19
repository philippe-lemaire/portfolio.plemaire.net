from django.urls import path
from django.views.generic import TemplateView

app_name = "contactme"

urlpatterns = [
    path("", TemplateView.as_view(template_name="contactme/index.html"), name="index"),
]
