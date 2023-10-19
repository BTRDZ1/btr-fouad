from django.shortcuts import render
from django.views.generic import ListView
from .models import ClientData

class ClientDataListView(ListView):
    model = ClientData
    template_name = 'custom_panel/clientdata_list.html'
    context_object_name = 'clientdata'
