from django.conf.urls import url
from . import views

app_name='stockindex'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addindex$', views.addindex, name='addindex'),
    url(r'^deleteindex$', views.deleteindex, name='deleteindex'),
    url(r'^(?P<stockindex_id>[0-9]+)/$', views.details, name='detail'),
    url(r'^(?P<stockindex_id>[0-9]+)/add/$', views.add, name='add'),
    url(r'^(?P<stockindex_id>[0-9]+)/modify/$', views.modify, name='modify'),
]
