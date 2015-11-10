from django.test import TestCase
from api.models import Todo


class TestListCreateTodos(TestCase):
    def setUp(self):
        Todo.objects.create(title='Test title 1')
        Todo.objects.create(title='Test title 2', completed=True, count=1)
        Todo.objects.create(title='Test title 3', count=4)

    def test_get(self):
        pass

    def test_post(self):
        pass

class TestDetailUpdateTodos(TestCase):

    def setUp(self):
        Todo.objects.create(title='Test title 1')
        Todo.objects.create(title='Test title 2', completed=True, count=1)
        Todo.objects.create(title='Test title 3', count=4)

    def test_get(self):
        pass

    def test_put(self):
        pass

