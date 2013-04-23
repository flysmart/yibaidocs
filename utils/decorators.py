# coding=utf-8
__author__ = 'laonan'

import json
from django.http import HttpResponse


def ajax_api(function=None, login_required=False, method=None):
    """Check the request if it's ajax request, if not, refuse it.
    """

    def _dec(view_func):
        def _view(request, *args, **kwargs):

            if not request.is_ajax():
                return HttpResponse('403 Forbidden!', status=403)
            else:
                if method and (request.method.upper() != method.upper()):
                    return HttpResponse('403 Forbidden!', status=403)

                if login_required:
                    if request.user.is_authenticated():
                        return view_func(request, *args, **kwargs)
                    else:
                        json_result = {'status' : -2, 'message' : 'Login Expired.'}
                        return HttpResponse(json.dumps(json_result), 'application/json')
                else:
                    return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)