from django.contrib import admin
from .models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_filter = ['name', 'location', 'frequency', 'instructions', 'start', 'end', 'added', 'changed']
    list_display = ['name', 'location', 'frequency', 'instructions', 'start', 'end', 'added', 'changed']
