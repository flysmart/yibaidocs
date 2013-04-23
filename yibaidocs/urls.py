from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index',{'template_name' : 'home.html'}, name='home'),
    url(r'^login/$', 'account.views.login', {'template_name' : 'login.html'}, name='login'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^password/reset/$', 'account.views.reset_password', {'template_name' : 'reset_password.html'}, name='reset_password'),
    # url(r'^yibaidocs/', include('yibaidocs.foo.urls')),

    url(r'^certificate\.cert$', RedirectView.as_view(url= '/static/certificate.cert')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/home/$', 'doc.views.home', {'template_name' : 'docs_home.html'}),
    url(r'^docs/api/(?P<application_code>[\w|-]+)/$', 'doc.views.api_home', {'template_name' : 'api_home.html'}),
    url(r'^doc/(?P<doc_id>\d+)/$', 'doc.views.doc', {'template_name' : 'api_doc.html'}),
    url(r'^schedule/(?P<application_code>[\w|-]+)/$', 'schedule.views.daily_schedule', {'template_name' : 'schedule.html'}),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^js/global\.js', 'utils.views.global_js'),
    url(r'^mark-my-tasks/$', 'account.views.mark_my_tasks'),
    url(r'^submit-feedback/$', 'schedule.views.submit_feedback'),
    url(r'^get-feedback/$', 'schedule.views.get_feedback'),
)
