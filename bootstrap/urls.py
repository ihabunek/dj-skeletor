from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('bootstrap.views',
    url(r'^$', 'hello_fixed', name='bootstrap_hello_fixed'),
    url(r'^fluid/$', 'hello_fluid', name='bootstrap_hello_fluid'),
)
