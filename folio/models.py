from django.db import models
from datetime import time
from django.db.models.deletion import CASCADE
from django.utils import timezone
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.contrib import admin

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=35)
    slug = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    summary = models.TextField()
    content = MarkdownxField()
    pub_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="projects")
    git_repo = models.URLField(blank=True)
    deployed_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    # Create a property that returns the markdown instead
    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    @admin.display(
        ordering="pub_date",
        description="Published?",
        boolean=True,
    )
    def is_published(self):
        return self.published
