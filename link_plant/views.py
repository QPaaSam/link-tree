from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    model = Link

class LinkCreateView(CreateView):
    model = Link
    fields = '__all__'
    success_url = reverse_lazy('link-list')