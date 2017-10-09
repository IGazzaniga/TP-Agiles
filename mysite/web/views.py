from django.shortcuts import render
from django.views import View
from django.utils import timezone
from models import Novedad

# Create your views here.
def web_view(request):
    """Returns the website."""
    novedades = Novedad.objects.all().order_by('-fechaP')[:5]
    return render(request, 'web/index.html', {'novedades': novedades})

   