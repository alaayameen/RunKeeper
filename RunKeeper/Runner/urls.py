from django.conf.urls import url

from . import views


app_name = 'runner'
urlpatterns = [
    
    url(r'^$', views.SessionsListView.as_view(), name='sessions'),
    url(r'^distance/$', views.SessionsDistanceDetailView.as_view(), name='distance'),
    url(r'^(?P<pk>[0-9]+)/speed/$', views.SessionSpeedDetailView.as_view(), name='speed'),
    url(r'^(?P<pk>[0-9]+)/$', views.SessionDetailView.as_view(), name='session'),
    url(r'^speed/average/$', views.SessionsAverageSpeedDetailView.as_view(), name='averageSpeed'),
    url(r'^create/$', views.CreateSessionFormView.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.DeleteSessionView.as_view(), name='delete'),

]
