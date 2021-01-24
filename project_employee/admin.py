from django.contrib import admin
from .models import ProjectEmployee

class ProjectAdmin(admin.ModelAdmin):
	pass

admin.site.register(ProjectEmployee, ProjectAdmin)

