from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from .models import Task


class CreateTaskTests(TestCase):

    def test_create_one_task(self):
        task = Task.objects.create(text='task', time=now())

        response = self.client.get(reverse('todo:index'))

        self.assertQuerysetEqual(
            response.context['task_list'],
            [task]
        )

    def test_create_two_tasks(self):
        task1 = Task.objects.create(text='first task', time=now())
        task2 = Task.objects.create(text='second task', time=now())

        response = self.client.get(reverse('todo:index'))

        self.assertQuerysetEqual(
            response.context['task_list'],
            [task1, task2]
        )
