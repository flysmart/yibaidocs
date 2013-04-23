import json

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponse

def global_js(request):
    if not cache.get('js_global_variables'):
        global_variables = list()
        static_url = 'var static_url = "%s";' %settings.STATIC_URL
        mark_my_tasks_url = 'var g_mark_my_tasks_url = "%s";' %reverse('account.views.mark_my_tasks')
        submit_feedback_url = 'var g_submit_feedback_url = "%s";' %reverse('schedule.views.submit_feedback')
        get_feedback_url = 'var g_get_feedback_url = "%s";' %reverse('schedule.views.get_feedback')


        global_variables.append(static_url)
        global_variables.append(mark_my_tasks_url)
        global_variables.append(submit_feedback_url)
        global_variables.append(get_feedback_url)

        cache.set('js_global_variables', ''.join(global_variables), 60*60)


    return HttpResponse(cache.get('js_global_variables'), mimetype='application/javascript')

