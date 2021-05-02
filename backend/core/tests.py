from rest_framework.test import APIClient

from django.test import TestCase

from .models import Todo

__all__ = ['TodoTestCase']


class TodoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def test_todo_crud(self):
        # create test
        todo = Todo.objects.create(title='buy some milk')
        self.assertEqual(todo.id, todo.pk)

        # read test
        todo = Todo.objects.first()
        self.assertEqual(str(todo), 'buy some milk')

        # update test
        old_value = todo.is_completed
        todo.is_completed = True
        todo.save()

        self.assertFalse(old_value)
        self.assertTrue(Todo.objects.get(id=todo.id).is_completed)

        # delete test
        deletes = todo.delete()
        self.assertEqual(str(deletes), "(1, {'core.Todo': 1})")


class TodoApiTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.api_client = APIClient()

    def test_create_todo(self):
        response = self.api_client.post('/api/todo/',
                                        {'title': 'buy some milk'})
        self.assertEqual(response.status_code, 201)

    def test_list_todo(self):
        for i in range(5):
            Todo.objects.create(title=f'example title {i}')

        response = self.api_client.get('/api/todo/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 5)

    def test_update_todo(self):
        todo = Todo.objects.create(title=f'buy some milk')

        data = {
            "title": "buy some bread",
            "body": "...",
            "is_completed": True
        }
        response = self.api_client.put(f'/api/todo/{todo.id}/', data)
        self.assertEqual(response.status_code, 200)

        response = self.api_client.get(f'/api/todo/{todo.pk}/')
        response_json = response.json()

        self.assertEqual(response_json.get('title'), "buy some bread")

    def test_delete_todo(self):
        todo = Todo.objects.create(title=f'buy some milk')

        response = self.api_client.delete(f'/api/todo/{todo.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Todo.objects.count(), 0)
