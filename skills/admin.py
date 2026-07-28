from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency', 'is_tool', 'order')
    list_filter = ('category', 'is_tool')
    list_editable = ('order', 'proficiency')
    search_fields = ('name',)
