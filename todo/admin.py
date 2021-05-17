from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('text', 'time')
    readonly_fields = ('pk', )
    fields = ['pk', 'text', 'time', 'done']


admin.site.register(Task, TaskAdmin)
