from django.urls import path, re_path
from .views import Tasks, Remove

app_name = 'todo_app'

urlpatterns = [
    path('', Tasks.as_view(), name = 'items'),
    re_path(r'^remove/item/(?P<slug>[-\w]+)/$', Remove.as_view(), name='item_remove'),
]
