from django.shortcuts import (redirect, render)
from django.views import View
from django.utils import timezone
from .models import Novedad, Trabajo, Investigacion

# Create your views here.
def web_view(request):
    """Returns the website."""
    novedades = Novedad.objects.all().order_by('-fechaP')[:5]
    return render(request, 'web/index.html', {'novedades': novedades})

def id_list(request):
    """Return a list of i+d topics."""
    ids = Investigacion.objects.all()  
    return render(request, 'web/id.html', {'ids': ids})

def jobs_list(request):
    """Returns a list of jobs"""
    trabajos = Trabajo.objects.all()
    return render(request, 'web/jobs.html', {'trabajos': trabajos})

   