from django.shortcuts import render
from .models import formulario
from django.views import generic
# Create your views here.
def index (request):
    num_Formu = formulario.objects.all().count()

    return render(
        request,
        'index.html',
        context={'nun_formu': num_Formu},
    )