from django.contrib import admin
from .models import Project, Tag
from markdownx.admin import MarkdownxModelAdmin

# Register your models here.


class ProjectAdmin(MarkdownxModelAdmin):
    list_display = [
        "title",
        "is_published",
        "pub_date",
    ]
    list_filter = ["pub_date"]


admin.site.register(Tag)
admin.site.register(Project, ProjectAdmin)
