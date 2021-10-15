from typing import Text
from django.test import TestCase
import ToDoApp
from ToDoApp.models import TODO

class TestModels(TestCase):

    def setUp(self):
        self.task1=TODO.objects.create(
            text="Eat Breakfast"
        )
    