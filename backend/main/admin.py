from django.contrib import admin
from .models import Contact, Tool, Project, Skill

# Register your models here.

admin.site.register(Contact)
admin.site.register(Tool)
admin.site.register(Project)
admin.site.register(Skill)
