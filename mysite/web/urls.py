"""Web urls."""

from django.conf.urls import include, url
from . import views
from web.views import web_view #Importamos la vista


urlpatterns = [
    url(r'^web/', web_view),
]