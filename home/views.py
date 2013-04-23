# coding=utf-8

from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@csrf_exempt
def test_post(request):
    if request.method == 'POST':
        return HttpResponse('post.')
    else:
        return HttpResponse('get')

def index(request, template_name):
    template_var = {}
    return render_to_response(template_name, template_var, context_instance=RequestContext(request))