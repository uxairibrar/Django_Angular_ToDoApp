from django.http import response
from django.test import TestCase,Client
from django.urls import reverse
from ToDoApp.models import TODO
import json

class TestView(TestCase):
    
    def setUp(self):
        self.client=Client()
        self.todo_url=reverse('todo')
        self.project1=TODO.objects.create(
            text="Check"
        )

    # It tests the get method of todo view 
    def test_todo_list_GET(self):
        response=self.client.get(self.todo_url)
        self.assertEquals(response.status_code,200)
