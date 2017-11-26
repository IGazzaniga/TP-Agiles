from django.contrib import admin

# Register your models here.
from .models import Novedad
from .models import Trabajo
from .models import Investigacion

class NovedadAdmin(admin.ModelAdmin):
    fields = ['titulo', 'contenido', 'fechaP']

admin.site.register(Novedad, NovedadAdmin)

class TrabajoAdmin(admin.ModelAdmin):
    fields = ['titulo','descripcion','fechaP','disponible']

admin.site.register(Trabajo, TrabajoAdmin)

class InvestigacionAdmin(admin.ModelAdmin):
    fields = ['titulo', 'autor', 'archivo']

admin.site.register(Investigacion, InvestigacionAdmin)