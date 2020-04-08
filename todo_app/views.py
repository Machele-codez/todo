from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Tasks(LoginRequiredMixin, generic.CreateView):
    model = Task  
    template_name = 'todo_app/task_list.html'
    success_url = reverse_lazy('tasks:items')
    form_class = TaskForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class Remove(generic.RedirectView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Task, slug=self.kwargs.get('slug'))
        item.delete()
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('tasks:items')



