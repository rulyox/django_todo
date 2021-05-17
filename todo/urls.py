from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [

    # Web GUI
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('done/<int:task_id>', views.done_by_id, name='done-by-id'),
    path('update/<int:task_id>', views.update_by_id, name='update-by-id'),
    path('delete/<int:task_id>', views.delete_by_id, name='delete-by-id'),

    # REST API
    path('api/all', views.AllAPI.as_view(), name='api-all'),  # GET
    path('api/add', views.AddAPI.as_view(), name='api-add'),  # POST
    path('api/<int:task_id>', views.ByIdAPI.as_view(), name='api-by-id')  # GET, PUT, DELETE

]
