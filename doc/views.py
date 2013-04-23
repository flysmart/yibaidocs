# coding=utf-8
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404

from doc.models import APICategory, APIDoc, ProjectCode
from utils.snippets import _get_apps, _get_app

@login_required(login_url='/login')
def home(request, template_name):

    codes = ProjectCode.objects.all()

    template_var = dict()
    template_var['codes'] = codes
    template_var['high_light_code'] = 'home'
    template_var['apps'] = _get_apps()
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@login_required(login_url='/login')
def api_home(request, application_code, template_name):
    template_var = dict()

    apps = _get_apps()
    app = _get_app(apps, application_code)
    categories = APICategory.objects.filter(app=app)

    template_var['high_light_code'] = application_code
    template_var['apps'] = apps
    template_var['app'] = app
    template_var['categories'] = categories
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@login_required(login_url='/login')
def doc(request, doc_id, template_name):
    template_var = dict()
    apps = _get_apps()
    try:
        doc = APIDoc.objects.get(id=doc_id)
    except APIDoc.DoesNotExist:
        raise Http404

    template_var['doc'] = doc
    template_var['apps'] = apps
    template_var['high_light_code'] = doc.app.code
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))