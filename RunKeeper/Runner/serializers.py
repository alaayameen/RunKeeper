'''
Created on Aug 9, 2016

@author: ayameen
'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Runner.models import RunSession
from django.shortcuts import get_object_or_404


class SessionsListSerializer(serializers.Serializer):
    
    distance = serializers.IntegerField()
    duration = serializers.IntegerField()
 
    def create(self, validated_data):
        return RunSession.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.distance = validated_data.get('distance', instance.distance)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance
    
    
        
    
    class Meta:
        model = RunSession
        fields = ('distance', 'duration')
