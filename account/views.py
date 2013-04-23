# coding=utf-8
import json
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

from utils.decorators import ajax_api

def login(request, template_name):
    template_var = {}
    next_url = request.GET.get('next')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user:
            auth_login(request,user)
            if next_url:
                return HttpResponseRedirect(next_url)
            else:
                return HttpResponseRedirect(reverse('doc.views.home'))
        else:
            template_var['login_failure'] = True
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('doc.views.home'))

    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@login_required(login_url='/login')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('account.views.login'))

@login_required(login_url='/login')
def docs(request, template_name):
    template_var = {}
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@login_required(login_url='/login')
def reset_password(request, template_name):
    template_var = {}
    if request.method == 'POST':
        old_password = request.POST.get('old_password', None)
        new_password = request.POST.get('new_password', None)
        confirm_password = request.POST.get('confirm_password', None)

        if new_password != confirm_password:
            template_var['failure_message'] = u'两次新密码输入不一样'
            return render_to_response(template_name, template_var, context_instance=RequestContext(request))

        if old_password:
            user = authenticate(username=request.user.username, password=old_password)
            if user:

                user.set_password(new_password)
                user.save()
                return HttpResponseRedirect(reverse('doc.views.home'))
            else:
                template_var['failure_message'] = u'原密码错误'
        else:
            template_var['failure_message'] = u'请输入原密码'

    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@ajax_api(login_required=True, method='GET')
def mark_my_tasks(request):
    mark_my_tasks = request.GET.get('mark_my_tasks')

    profile = request.user.get_profile()
    profile.mark_my_tasks = False if mark_my_tasks == 'false' else True
    profile.save()

    j = {'saved' : True, 'mark_my_tasks' : mark_my_tasks}

    return HttpResponse(json.dumps(j))
