# coding=utf-8
from django.contrib import admin
from doc.models import ProjectCode, Application, APICategory, APIDoc

class ProjectCodeAdmin(admin.ModelAdmin):
    list_display = ('pk','code', 'desc', 'available', 'create_datetime')
    ordering = ('-create_datetime',)
    search_fields = ('code',)
admin.site.register(ProjectCode, ProjectCodeAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'code', 'desc', 'create_datetime')
    ordering = ('-create_datetime',)
    search_fields = ('name',)
admin.site.register(Application, ApplicationAdmin)

class APICategoryAdmin(admin.ModelAdmin):
    list_display = ('pk','app', 'name', 'code', 'create_datetime')
    list_filter = ('app',)
    ordering = ('-create_datetime',)
    search_fields = ('name',)
admin.site.register(APICategory, APICategoryAdmin)

class APIDocAdmin(admin.ModelAdmin):
    list_display = ('pk','app', 'category', 'name', 'desc', 'create_datetime', 'update_datetime')
    list_filter = ('category',)
    ordering = ('-create_datetime',)
    search_fields = ('name',)
admin.site.register(APIDoc, APIDocAdmin)