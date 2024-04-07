from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import TrainForm

from .models import Train


class Home(ListView):
    model = Train
    context_object_name = 'trains'
    template_name = 'train/index.html'


class Details(DetailView):
    model = Train
    context_object_name = 'train'
    template_name = 'train/details.html'


class CrForm(SuccessMessageMixin, CreateView):
    model = Train
    form_class = TrainForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('home')
    success_message = "Post created "


class UpdateCiti(SuccessMessageMixin, UpdateView):
    model = Train
    form_class = TrainForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('home')
    success_message = "Post updated "


class DeleteCiti(DeleteView):
    model = Train
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Profile deleted")
        return self.post(request, *args, **kwargs)
