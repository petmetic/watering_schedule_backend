from django.contrib import admin
from .models import Plant



@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_filter = ['name', 'location', 'frequency', 'volume', 'instructions', 'status','start', 'end','photo', 'added', 'changed']
    list_display = ['name', 'location', 'frequency', 'volume', 'instructions', 'status','start', 'end','photo', 'added', 'changed']

