from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project, Tag

# Create your views here.


class ProjectListView(ListView):
    model = Project

    def get_queryset(self):
        queryset = Project.objects.filter(published=True)
        return queryset


class ProjectDetailView(DetailView):
    model = Project


class TagDetailView(DetailView):
    model = Tag
