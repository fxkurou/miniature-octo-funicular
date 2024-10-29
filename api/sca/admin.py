from django.contrib import admin
from .models import SpyCat, Mission, Target

@admin.register(SpyCat)
class SpyCatAdmin(admin.ModelAdmin):
    list_display = ['name', 'years_of_experience', 'breed', 'salary', 'is_available']
    list_editable = ['is_available']
    search_fields = ['name']
    ordering = ['name']

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['cat', 'is_completed']
    list_editable = ['is_completed']
    search_fields = ['cat__name']
    ordering = ['cat__name']

@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'notes', 'is_complete']
    list_editable = ['is_complete']
    search_fields = ['name']
    ordering = ['name']