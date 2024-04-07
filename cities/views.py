from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CityForm

from .models import City


class Home(ListView):
    model = City
    context_object_name = 'cities'
    template_name = 'cities/index.html'


class Details(DetailView):
    model = City
    context_object_name = 'cities'
    template_name = 'cities/details.html'


class CrForm(SuccessMessageMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('home')
    success_message = "Post created "


class UpdateCiti(SuccessMessageMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('home')
    success_message = "Post updated "


class DeleteCiti(DeleteView):
    model = City
    # template_name = 'cities/delete.html'
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        messages.success(request, "Profile deleted")
        return self.post(request, *args, **kwargs)
