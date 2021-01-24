from django.contrib import admin
from .models import WorksOn

class WorksOnAdmin(admin.ModelAdmin):
	pass

admin.site.register(WorksOn, WorksOnAdmin)
