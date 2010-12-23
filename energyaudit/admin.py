from energyaudit.models import *
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *

admin.site.unregister(Site)
#admin.site.unregister(User)
admin.site.unregister(Group)

class clienteAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'raz_social')
    #search_fields = ('numero_socio', 'nombre', 'apellido')
	def queryset(self, request):
		qs = super(clienteAdmin, self).queryset(request)
		return qs.filter(user=request.user)

class edificioAdmin(admin.ModelAdmin):
        def queryset(self, request):
                qs = super(edificioAdmin, self).queryset(request)
                return qs.filter(user=request.user)

class ambienteAdmin(admin.ModelAdmin):
        def queryset(self, request):
                qs = super(ambienteAdmin, self).queryset(request)
                return qs.filter(user=request.user)

class paredAdmin(admin.ModelAdmin):
	list_display = ('ambiente_pared',)



class artefactoAdmin(admin.ModelAdmin):
        def queryset(self, request):
                qs = super(artefactoAdmin, self).queryset(request)
                return qs.filter(user=request.user)
class contactoAdmin(admin.ModelAdmin):
        def queryset(self, request):
                qs = super(contactoAdmin, self).queryset(request)
                return qs.filter(user=request.user)



admin.site.register(cliente,clienteAdmin)
admin.site.register(edificio,edificioAdmin)
admin.site.register(ambiente)
admin.site.register(pared,paredAdmin)
admin.site.register(artefacto)
admin.site.register(contacto)

