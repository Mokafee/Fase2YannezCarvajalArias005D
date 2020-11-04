from django.shortcuts import render
from .models import formulario
from django.views import generic
# Create your views here.

from django.generic_edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def contacto (request):
    num_Formu = formulario.objects.all().count()

    return render(
        request,
        'contacto.html',
        context={'nun_formu': num_Formu},
    )