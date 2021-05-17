import json
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def task_to_dict(task):
    return {
        'id': task.pk,
        'text': task.text,
        'time': str(task.time),
        'done': task.done
    }


def response_json(obj):
    return HttpResponse(json.dumps(obj), content_type='application/json')


def redirect_to_index():
    return HttpResponseRedirect(reverse('todo:index'))
