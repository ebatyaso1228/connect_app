from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from .models import ConnectModel
from django.urls import reverse_lazy


# Create your views here.
class ConnectList(ListView):
    template_name = 'list.html'
    model = ConnectModel

class ConnectDetail(DetailView):
    template_name = 'detail.html'
    model = ConnectModel

class ConnectCreate(CreateView):
    template_name = 'create.html'
    model = ConnectModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')

class ConnectDelete(DeleteView):
    template_name = 'delete.html'
    model = ConnectModel
    success_url = reverse_lazy('list')

class ConnectUpdate(UpdateView):
    template_name = 'update.html'
    model = ConnectModel
    fields = ('title', 'memo')
    success_url = reverse_lazy('list')

    
