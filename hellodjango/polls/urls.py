from django.conf.urls import patterns, url

from polls import views
from django.views import generic
from polls.models import Poll

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/results/$', generic.DetailView.as_view(
        model=Poll, template_name='polls/result.html'), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
