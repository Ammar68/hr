from django.contrib import admin
from .models import Department


class DepartmentAdmin(admin.ModelAdmin):
	"""TO DO ADMIN ACTIONS HERE"""
	pass

admin.site.register(Department, DepartmentAdmin)
