# coding=utf-8
from django.contrib import admin
from schedule.models import WorkingDay, Feedback

class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ('pk','app', 'year', 'month', 'day', 'create_datetime')
    list_filter = ('app',)
    ordering = ('-create_datetime',)
    search_fields = ('desc',)
admin.site.register(WorkingDay, WorkingDayAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'working_day', 'feedback', 'create_datetime')
    list_filter = ('user',)
    ordering = ('-create_datetime',)
    search_fields = ('feedback',)
admin.site.register(Feedback, FeedbackAdmin)
