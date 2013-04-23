# coding=utf-8
import json
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from utils.snippets import _get_apps, _get_app
from utils.decorators import ajax_api
from schedule.models import WorkingDay, Feedback

@login_required(login_url='/login')
def daily_schedule(request, application_code, template_name):
    template_var = {}
    apps = _get_apps()
    app = _get_app(apps, application_code)

    working_days = WorkingDay.objects.filter(app = app)
    paginator = Paginator(working_days, 31)
    page = int(request.GET.get('page', '1'))

    try:
        working_days = paginator.page(page)
    except (EmptyPage, InvalidPage):
        working_days = paginator.page(paginator.num_pages)

    template_var['s_high_light_code'] = application_code
    template_var['working_days'] = working_days
    template_var['apps'] = apps
    template_var['app'] = app
    template_var['mark_my_tasks'] = request.user.get_profile().mark_my_tasks
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))

@ajax_api(login_required=True, method='POST')
def submit_feedback(request):
    try:
        feedback = Feedback()
        feedback.user = request.user
        feedback.nick_name = request.user.first_name + request.user.last_name
        feedback.feedback = request.POST.get('feedback')
        feedback.working_day = WorkingDay.objects.get(id=request.POST.get('workingday_id'))
        feedback.save()
        json_str = '{"status" : 1, "message" : "ok"}'
    except Exception, e:
        json_str = '{"status" : -1, "message" : "%s"}' %str(e)

    return HttpResponse(json_str)

@ajax_api(login_required=True, method='GET')
def get_feedback(request):

    workingday_id = request.GET.get('workingday_id')
    working_day = WorkingDay.objects.get(id=workingday_id)
    feedback = Feedback.objects.filter(working_day=working_day)

    from django.core import serializers
    data = serializers.serialize('json', feedback)
    data = {'items' : data, 'workingday_id' : workingday_id}

    return HttpResponse(json.dumps(data))
    
