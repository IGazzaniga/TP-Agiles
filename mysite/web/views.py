from django.shortcuts import render
from django.views import View

# Create your views here.
def web_view(request):
    """Returns the website."""
    return render(request, 'web/index.html', {})