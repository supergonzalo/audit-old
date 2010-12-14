
from django.shortcuts import render_to_response
from energyaudit.models import *
from django.contrib.auth.models import User

def tabs(request):
        return {'tabs':request.user.is_authenticated()}

def body(request,sel):
	links={'profile':get_info,'score':get_score}
	return links.get(sel,link_not_found)(request)

def link_not_found(request):
	return ["not_found.html",{}]

def get_score(request):
        #obtener el nombre de usuario
        u=User.objects.get(username=request.user.username)
        #obtener los edificios que tiene esos codigos
        e=edificio.objects.filter(user=u)
        variables_informe=dict()
        variables_informe['tabs']=tabs(request)
        variables_informe['barra']=['FB0200','FF8000','FFCA01','FFE000','FFFF00','CFE500','95E500','80E501','50F000','00FF03']
	variables_informe['score']=['','','','','','Indice Actual','','Indice Potencial','','']
	variables_informe['average']=['','','','','','','','','','']
	variables_informe['edificios']=e
        return ["scorecard.html",variables_informe]

def get_info(request):
	#obtener el nombre de usuario
	u=User.objects.get(username=request.user.username)
	#obtener los edificios que tiene esos codigos
	e=edificio.objects.filter(user=u)
	variables_informe=dict()
	variables_informe['tabs']=tabs(request)
        variables_informe['col1']='Info'
        variables_informe['edificios']=e
        variables_informe['intro']='get_info'
        variables_informe['proyeccion_consumo_anual']=''
        variables_informe['proyeccion_consumo_mensual']=''
        variables_informe['consumo_por_ambiente']=''
        variables_informe['fuera_de_horario']=''
        variables_informe['conclusiones']=''
        variables_informe['sponsors']='Estos son los Sponsors'
	return ["informe.html",variables_informe]

def graficos(request,tipo):
        values={'t':'totales.png','a':'a.png','b':'b.png','c':'c.png'}
        return open(os.getcwd() + "/templates/" + values[tipo], "rb").read()

def cuadro_consumo(request):

        #for ambiente in edificio, [ambiente,refrigeracion,calefaccion,iluminacion,otro]

        cuadro=[['Oficina principal primer piso',2,3,4,5,25],['Recepcion primer piso',6,7,8,9,25]]
        return cuadro


