from energyaudit.models import *
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *

#if 
admin.site.unregister(Site)
admin.site.unregister(User)
admin.site.unregister(Group)

class clienteAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'raz_social')
    #search_fields = ('numero_socio', 'nombre', 'apellido')




admin.site.register(cliente,clienteAdmin)
admin.site.register(edificio)
admin.site.register(ambiente)
admin.site.register(pared)
admin.site.register(artefacto)
admin.site.register(contacto)

