from django.test import TestCase
from django.test.client import Client
from rest_framework.reverse import reverse_lazy
from Runner.models import RunSession
from Runner.serializers import SessionsListSerializer


class SessionViewTest(TestCase):
    
    
    fixtures = ['initial_data.json', 'auth.json', 'authtoken.json']
           
    def test_create_session_view(self):
        
            session = RunSession.objects.create(distance=100, duration=100)
            sessionJson = SessionsListSerializer(session)
            url = reverse_lazy("runner_api:apiCreate")
            resp = self.client.post(url, sessionJson, "application/json")
            self.assertEqual(resp.status_code, 201)
            
    def test_create_session_view_2(self):
        
            
            client = Client(HTTP_AUTHORIZATION='Token 2aff6490fd1c30ce46b3589e0b231f49e0c12ca7')
            session = RunSession.objects.create(distance=100, duration=100)
            sessionJson = SessionsListSerializer(session)
            
            url = reverse_lazy("runner_api:apiCreate")
            resp = client.post(url, sessionJson, "application/json", Authorization='Token 2aff6490fd1c30ce46b3589e0b231f49e0c12ca7')
            self.assertEqual(resp.status_code, 201)
            
    def test_update_session_view_1(self):
        
            session = RunSession.objects.create(distance=100, duration=100)
            sessionJson = SessionsListSerializer(session)
            
            url = reverse_lazy("runner_api:apiUpdate", kwargs={'pk': 26})
            resp = self.client.put(url, sessionJson, "application/json")
            self.assertEqual(resp.status_code, 200)
            
    def test_update_session_view_2(self):
        
            session = RunSession.objects.create(distance=100, duration=100)
            sessionJson = SessionsListSerializer(session)
                    
            url = reverse_lazy("runner_api:apiUpdate", kwargs={'pk': 2000})
            resp = self.client.put(url, sessionJson, "application/json")
            self.assertEqual(resp.status_code, 200)
            
    def test_get_session_view_1(self):
            
            client = Client(HTTP_AUTHORIZATION='Token 2aff6490fd1c30ce46b3589e0b231f49e0c12ca7')
            url = reverse_lazy("runner_api:apiView", kwargs={'pk': 26})
            request = client.get(url)
            self.assertEqual(request, 200)
            
    def test_get_session_view_2(self):
        
            url = reverse_lazy("runner_api:apiView", kwargs={'pk': 2000})
            resp = self.client.get(url)
            self.assertEqual(resp.status_code, 404)
