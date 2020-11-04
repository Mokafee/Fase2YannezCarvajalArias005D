from django.shortcuts import render
from .models import formulario
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from noticias.views import index


def contacto (request):
    return render(
        request,
        'contacto.html',
    )

    index(request):
    return render(request, 'index.html')

class ContactoCreate(CreateView):
    model = contacto
    fields = '__all__'
    initial = {'name', 'email', 'telefono', 'massage'}

class ContactoUpdate(UpdateView):
    model = contacto
    fields = {'name', 'email', 'telefono', 'massage'}

class ContactoDelete(DeleteView):
    model = contacto
    sucess_url = reverse_lazy('contactos')

class ContactoDetailView(generic.DetailView):
    model = contacto
