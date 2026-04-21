from django.contrib import admin
from .models import Skill, Project, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'order', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['skills']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'received_at', 'is_read']
    readonly_fields = ['name', 'email', 'message', 'received_at']

    