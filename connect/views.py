from django.shortcuts import render
from django.views.generic import ListView
from .models import ConnectModel

# Create your views here.
class ConnectList(ListView):
    template_name = 'list.html'
    model = ConnectModel