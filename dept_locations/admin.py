from django.contrib import admin
from .models import DeptLocations

class DeptLocationsAdmin(admin.ModelAdmin):
	pass

admin.site.register(DeptLocations, DeptLocationsAdmin)
