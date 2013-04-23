# coding=utf-8
__author__ = 'Alan'
from doc.models import Application

def _get_apps():
    apps = Application.objects.all()
    return apps

def _get_app(apps, code):
    for app in apps:
        if app.code == code:
            return app
