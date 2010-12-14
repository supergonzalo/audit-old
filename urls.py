from django.conf.urls.defaults import *
from django.contrib.auth import authenticate, login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'energyaudit.views.general'),
  (r'(head)', 'energyaudit.views.formato'),

  (r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'}),
  (r'^logout/$','django.contrib.auth.views.logout',{'next_page':'/'}),

  (r'^accounts/([a-z]*)/$', 'energyaudit.views.account'),
  (r'^contact/$','energyaudit.views.contacto'),
  (r'^admin/', include(admin.site.urls)),

  #Auxiliares de Graficos
  (r'^accounts/profile/(score.png)$','energyaudit.views.graficos'),
  (r'^accounts/profile/(d_anual.png)$','energyaudit.views.graficos'),
  (r'^accounts/profile/(mensual.png)$','energyaudit.views.graficos'),
  (r'^accounts/profile/(end_use.png)$','energyaudit.views.graficos'),

)


