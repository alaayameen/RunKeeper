from django.conf.urls import url

from . import views


app_name = 'runner_api'
urlpatterns = [
    
    url(r'^$', views.SessionsListAPIView.as_view(), name='apiSessions'),
    url(r'^(?P<pk>[0-9]+)/$', views.GetSessionAPIView.as_view(), name='apiView'),
    url(r'^(?P<pk>[0-9]+)/update$', views.UpdateSessionAPIView.as_view(), name='apiUpdate'),
    url(r'^(?P<pk>[0-9]+)/delete$', views.DeleteSessionAPIView.as_view(), name='apiDelete'),
    url(r'^create$', views.CreateSessionAPIView.as_view(), name='apiCreate'),
    url(r'^distance/$', views.SessionsDistanceDetailAPIView.as_view(), name='apiDistance'),
    url(r'^(?P<pk>[0-9]+)/speed/$', views.SessionSpeedDetailAPIView.as_view(), name='apiSpeed'),
    url(r'^speed/average/$', views.SessionsAverageSpeedDetailAPIView.as_view(), name='apiAverageSpeed'),

]
