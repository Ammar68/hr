from django.contrib import admin
from .models import DependentName

class DependentAdmin(admin.ModelAdmin):
	pass

admin.site.register(DependentName, DependentAdmin)
