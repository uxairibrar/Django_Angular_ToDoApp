from django.test import SimpleTestCase
from django.urls import reverse,resolve
# from views import TODOApi

from ToDoApp.views import TODOApi

# It tests the url of the todoapp
class TestUrls(SimpleTestCase):
    def test_todo_url_is_resolved(self):
        found = resolve('/todo/')  
        self.assertEqual(found.func, TODOApi)