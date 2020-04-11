from django.urls import path, re_path
from .views import Tasks, Remove, Complete, CompletedTasks

app_name = 'todo_app'

urlpatterns = [
    path('', Tasks.as_view(), name = 'items'),
    re_path(r'^remove/task/(?P<pk>\d+)/$', Remove.as_view(), name='task_remove'),
    re_path(r'^complete/task/(?P<pk>\d+)/$', Complete.as_view(), name='task_complete'),
    path('completed/', CompletedTasks.as_view(), name = 'completed'),
]
