import json
from django.views import View
from django.http import HttpResponse, HttpResponseBadRequest, Http404
from django.shortcuts import render
from django.utils.timezone import now
from .models import Task
from .utility import task_to_dict, response_json, redirect_to_index


# Web GUI

def index(request):
    task_list = Task.objects.all().order_by('pk')

    context = {
        'task_list': task_list
    }

    return render(request, 'todo/index.html', context)


def add(request):
    # parse body
    try:
        text = request.POST['text']
    except KeyError:
        return HttpResponseBadRequest('Wrong request body')

    # create object
    task = Task(text=text, time=now(), done=False)
    task.save()

    return redirect_to_index()


def done_by_id(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')

    task.done = not task.done
    task.save()

    return redirect_to_index()


def update_by_id(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')

    # parse body
    try:
        text = request.POST['text']
    except KeyError:
        return HttpResponseBadRequest('Wrong request body')

    # update object
    task.text = text
    task.time = now()
    task.save()

    return redirect_to_index()


def delete_by_id(request, task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404('Task does not exist')

    task.delete()

    return redirect_to_index()


# REST API

class AllAPI(View):

    def get(self, request):
        task_list = Task.objects.all().order_by('pk')

        result = []

        for task in task_list:
            result.append(task_to_dict(task))

        return response_json(result)


class AddAPI(View):

    def post(self, request):
        # check body format
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Use json data in request body')

        # check body json key
        if 'text' not in body:
            return HttpResponseBadRequest('Missing key in request body')

        # create object
        text = str(body['text'])
        task = Task(text=text, time=now(), done=False)
        task.save()
        new_id = task.pk

        result = {
            'id': new_id
        }

        return response_json(result)


class ByIdAPI(View):

    def get(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')

        result = task_to_dict(task)

        return response_json(result)

    def put(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')

        # check body format
        try:
            body = json.loads(request.body)
        except json.JSONDecodeError:
            return HttpResponseBadRequest('Use json data in request body')

        # update object
        if 'text' in body:
            text = str(body['text'])
            task.text = text

        if 'done' in body:
            done = bool(body['done'])
            task.done = done

        task.time = now()
        task.save()

        result = task_to_dict(task)

        return response_json(result)

    def delete(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
        except Task.DoesNotExist:
            raise Http404('Task does not exist')

        task.delete()

        return HttpResponse('deleted')
