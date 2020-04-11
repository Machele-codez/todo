from django.urls import reverse_lazy
from django.views import generic
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime

# Create your views here.

class Tasks(LoginRequiredMixin, generic.CreateView):
    model = Task  
    template_name = 'todo_app/task_list.html'
    success_url = reverse_lazy('tasks:items')
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        print('done')
        return super().form_valid(form)

    def form_invalid(self, form):
        print("INVALID")
        return super().form_invalid(form)

#TODO: handles task removal(deletes them from database)
class Remove(generic.RedirectView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        item.delete()
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('tasks:items')


class Complete(generic.RedirectView):
    def get(self, request, *args, **kwargs):
        task = Task.objects.filter(pk=self.kwargs.get('pk'))
        task.update(completed=True)
        task.update(completed_on=datetime.datetime.now())
        #// task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        #// task.complete()
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('tasks:items')


class CompletedTasks(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo_app/completed_tasks.html'
    def get_queryset(self):
        queryset = Task.objects.filter(completed=True, user=self.request.user)
        return queryset
