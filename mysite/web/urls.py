"""Web urls."""

from django.conf.urls import include, url
from . import views
from web.views import web_view, id_list, jobs_list #Importamos las vistas



urlpatterns = [
    url(r'^$', web_view),
    url(r'^id.html', id_list),
    url(r'^jobs.html', jobs_list)
]