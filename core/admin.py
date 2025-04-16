from django.contrib import admin

from core.models import ProjectFile, Customer, Project

# Register your models here.
admin.site.register(ProjectFile)
admin.site.register(Project)
admin.site.register(Customer)