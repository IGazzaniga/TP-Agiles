from django.shortcuts import render
from django.views import View
from django.utils import timezone
from .models import Novedad, Trabajo, Investigacion

# Create your views here.
def web_view(request):
    """Returns the website."""
    novedades = Novedad.objects.all().order_by('-fechaP')[:5]
    trabajos = Trabajo.objects.all().order_by('-fechaP')
    return render(request, 'web/index.html', {'novedades': novedades})

   