from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Shop
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    model = Shop

class ShopDetailView(DetailView):
    model=Shop

class ShopCreateView(CreateView):
    model=Shop
    fields='__all__'

class ShopUpdateView(UpdateView):
    model=Shop
    fields='__all__'

class ShopDeleteView(DeleteView):
    model=Shop
    success_url = reverse_lazy('lunchmap:index')