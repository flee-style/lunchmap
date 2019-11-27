from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Category,Shop
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Create your views here.
class IndexView(ListView):
    model = Shop

class ShopDetailView(DetailView):
    model=Shop

class ShopCreateView(LoginRequiredMixin,CreateView):
    model=Shop
    fields=['name','adress','category']#'__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView,self).form_valid(form)

class ShopUpdateView(LoginRequiredMixin,UpdateView):
    model=Shop
    fields=['name','adress','category']#'__all__'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('ユーザーが違うため編集できません')
        return super(UpdateView,self).dispatch(request,*args,**kwargs)

class ShopDeleteView(LoginRequiredMixin,DeleteView):
    model=Shop
    success_url = reverse_lazy('lunchmap:index')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('ユーザーが違うため削除できません')
        return super(DeleteView,self).dispatch(request,*args,**kwargs)