from django.contrib import admin

# Register your models here.
from .models import Novedad

class NovedadAdmin(admin.ModelAdmin):
    fields = ['titulo', 'contenido', 'fechaP', 'tags']

admin.site.register(Novedad, NovedadAdmin)