from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Item
from django.shortcuts import get_object_or_404
from .forms import ItemForm

# Create your views here.

class Items(generic.ListView, FormMixin):
    model = Item
    template_name = 'todo.html'
    context_object_name = 'tasks'
    form_class = ItemForm

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()
            return self.form_valid(form)
        else:
            self.object_list = Item.objects.all()
            return self.form_invalid(form)

    success_url = reverse_lazy('items')


# class Items(generic.CreateView, generic.ListView):
#     model = Item  
#     template_name = 'todo.html'
#     success_url = reverse_lazy('items')
#     form_class = ItemForm
#     context_object_name = 'tasks'

#     def form_invalid(self, form):
#         self.object_list = Item.objects.all()
#         return super().form_invalid(form)



class Remove(generic.RedirectView):
    def get(self, request, *args, **kwargs):
        item = get_object_or_404(Item, slug=self.kwargs.get('slug'))
        item.delete()
        return super().get(request, *args, **kwargs)
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('items')



