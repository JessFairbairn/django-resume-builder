from django.contrib import admin

from . import models

@admin.register(models.Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    ordering = ('user', 'title')


@admin.register(models.ResumeItem)
class ResumeItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'resume', 'company', 'start_date')
    ordering = ('user', '-start_date')
