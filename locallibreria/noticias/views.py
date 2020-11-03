from django.shortcuts import render
from .models import formulario
from django.views import generic
# Create your views here.
def contacto (request):
    num_Formu = formulario.objects.all().count()

    return render(
        request,
        'contacto.html',
        context={'nun_formu': num_Formu},
    )