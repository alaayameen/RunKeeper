from django.contrib import messages
from django.core import serializers
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, render_to_response
from django.views import generic
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, \
    permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.urls import template_name
from rest_framework.views import APIView
from Runner.models import RunSession
from Runner.serializers import SessionsListSerializer


@authentication_classes((SessionAuthentication, BasicAuthentication,))
@permission_classes((IsAuthenticated,))
class SessionsListView(generic.ListView):
    
    template_name = 'runSession/list.html'
    context_object_name = 'all_sessions_list'

    
    def get_queryset(self):
        """Return all sessions."""
        return RunSession.objects.all()

class SessionDetailView(generic.DetailView):
    model = RunSession
    context_object_name = 'session'
    template_name = 'runSession/sessionDetail.html'


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class SessionsDistanceDetailView(generic.DetailView):
    
    context_object_name = 'session'
    template_name = 'runSession/generalDetail.html'

    def get_object(self):
        """Return all sessions."""
        sessions = RunSession.objects.all()
        distance = 0
        for item in sessions:
            distance += item.distance
    
        context = {"distance": distance, "unit":"Miles"} 
        return (context)


@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class SessionsAverageSpeedDetailView(generic.DetailView):
    
    context_object_name = 'session'
    template_name = 'runSession/generalDetail.html'
    
    def get_object(self):
     
        roundedSpeed = calculateSpeed(None)   
        context = {"roundedSpeed": roundedSpeed, "unit":"Mile/Hour"} 
        return (context)



@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class SessionSpeedDetailView(generic.DetailView):
    
    context_object_name = 'session'
    template_name = 'runSession/generalDetail.html'
    
    def get_object(self, **kwargs):

        sessionId = self.kwargs['pk']
        roundedSpeed = calculateSpeed(sessionId)    
        context = {'roundedSpeed': roundedSpeed, 'unit':'Mile/Hour'}
        return (context)
    
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class DeleteSessionView(generic.DeleteView):
    
    template_name = 'runSession/confirm_delete.html'
    model = RunSession
    def get_success_url(self):
        return reverse('runner:sessions')
    
    
    
     
class CreateSessionFormView(generic.CreateView):
    
    is_created = False
    template_name = 'runSession/create.html'
    model = RunSession
    fields = ['distance', 'duration']
    
    # success_url = reverse('runner:speed', kwargs={'app_label': 'sessionID'})
    
    """ I had to use reverse_lazy because django reverse causes circular import,
        because the reverse is called when the module is imported, before the 
        urls have been loaded.
    """
    # First option to resolve
    # success_url = reverse_lazy('runner:sessions')
    
    # Second option, is to override the following method
    def get_success_url(self):
        return reverse('runner:sessions')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        self.is_created = True
        return super(CreateSessionFormView, self).form_valid(form)
     
    def get_context_data(self, **kwargs):
        
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            
        ctx = super(CreateSessionFormView, self).get_context_data(**kwargs)
        ctx['message'] = self.is_created
        return ctx
    
"""       
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
class CreateSessionView(generic.UpdateView):

    model = RunSession
    template_name = 'runSession/create'
    def get_object(self, queryset=None):

        # get the existing object or created a new one
        obj, created = RunSession.objects.get_or_create(col_1=self.kwargs['distance'], col_2=self.kwargs['duration'])

        return obj

"""
def calculateSpeed(sessionId):
    
    if sessionId == None:
        sessions =  RunSession.objects.all()
    else:
        arrayList = []
        session = get_object_or_404(RunSession, pk=sessionId)
        arrayList.append(session)
        sessions = arrayList
        
    totalDistance = 0
    totalTimeInSeconds = 0
    for item in sessions:
        totalDistance += item.distance
        totalTimeInSeconds += item.duration
    
    timeInHours = totalTimeInSeconds / 60
    averageSpeed = totalDistance / timeInHours
    roundedSpeed = round(averageSpeed, 2)
    
    return roundedSpeed


@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class GetSessionAPIView(APIView):
    
    def get(self, request, pk, format=None):
        
        session = get_object_or_404(RunSession, pk=pk)
        data = SessionsListSerializer(session)
        return Response(data.data)

@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class CreateSessionAPIView(APIView):
    def post(self, request, format=None):
       
        serializer = SessionsListSerializer(data=request.data)
        if serializer.is_valid():
             
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class UpdateSessionAPIView(APIView):
    def put(self, request, pk, format=None):
        
        runSession = get_object_or_404(RunSession, pk=pk)
        serializer = SessionsListSerializer(runSession, data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class DeleteSessionAPIView(APIView):

    def delete(self, request, pk, format=None):
        session = get_object_or_404(RunSession, pk=pk)
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
    
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class SessionsListAPIView(APIView):
    
    def get(self, request, format=None):
       
        data = SessionsListSerializer(RunSession.objects.all(), many=True)
        return Response(data.data)
    
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class SessionsDistanceDetailAPIView(APIView):
    
    def get(self, request):
        """Return all sessions."""
        sessions = RunSession.objects.all()
        distance = 0
        for item in sessions:
            distance += item.distance
    
        context = {"distance": distance, "unit":"Miles"} 
        return Response(context)
    
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class SessionsAverageSpeedDetailAPIView(APIView):
    
    def get(self, request):
     
        roundedSpeed = calculateSpeed(None)   
        context = {"roundedSpeed": roundedSpeed, "unit":"Mile/Hour"} 
        return Response (context)
        

@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
class SessionSpeedDetailAPIView(APIView):
    
    def get(self, request, pk):

        sessionId = pk
        roundedSpeed = calculateSpeed(sessionId)    
        context = {'roundedSpeed': roundedSpeed, 'unit':'Mile/Hour'}
        return Response (context)       
        
        