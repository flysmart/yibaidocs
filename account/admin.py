# coding=utf-8
from django.contrib import admin
from account.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'mark_my_tasks','desc', 'on_boarding_date')
    search_fields = ('user__username',)
admin.site.register(UserProfile, UserProfileAdmin)