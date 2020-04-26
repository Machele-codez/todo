from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView
from .forms import SignupForm

# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        logout(self.request)
        return super().form_valid(form)

