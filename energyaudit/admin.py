from energyaudit.models import *
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import *

admin.site.unregister(Site)
#admin.site.unregister(User)
admin.site.unregister(Group)

class edificioAdmin(admin.ModelAdmin):
	list_display = ('nombre_edif','direccion')
        def queryset(self, request):
                qs = super(edificioAdmin, self).queryset(request)
                return qs.filter(user=request.user)

class ambienteAdmin(admin.ModelAdmin):
	list_display = ('nombre_amb','nombre_edif')
        def queryset(self, request):
                qs = super(ambienteAdmin, self).queryset(request)
                return qs.filter(user=request.user)

class paredAdmin(admin.ModelAdmin):
	list_display = ('nombre_amb','orientacion_pared')
        def queryset(self, request):
                qs = super(paredAdmin, self).queryset(request)
                return qs.filter(user=request.user)


class artefactoAdmin(admin.ModelAdmin):
        def queryset(self, request):
                qs = super(artefactoAdmin, self).queryset(request)
                return qs.filter(user=request.user)
class contactoAdmin(admin.ModelAdmin):
	list_display = ('nombre_edif','nombre_pers')
        def queryset(self, request):
                qs = super(contactoAdmin, self).queryset(request)
                return qs.filter(user=request.user)



admin.site.register(edificio,edificioAdmin)
admin.site.register(ambiente,ambienteAdmin)
admin.site.register(pared,paredAdmin)
admin.site.register(artefacto,artefactoAdmin)
admin.site.register(contacto,contactoAdmin)

