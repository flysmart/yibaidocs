# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import force_unicode

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    desc = models.CharField(max_length=400, null = True, blank=True)
    mobile = models.IntegerField(default=20)
    mark_my_tasks = models.BooleanField(default=False)
    on_boarding_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.user.username.encode('utf-8')
    def __unicode__(self):
        return force_unicode(self.user.username)
    class Admin:
        pass