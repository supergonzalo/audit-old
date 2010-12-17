#!/bin/sh
from django.shortcuts import render_to_response
from energyaudit.models import *
from django.contrib.auth.models import User
from django.db import models


def tabs(request):
        return {'tabs':request.user.is_authenticated()}

def body(request,sel):
	links={'profile':get_info,'score':get_score}
	return links.get(sel,link_not_found)(request)

def link_not_found(request):
	return ["not_found.html",{}]

def head(request):
        class rate:
                color=''
                rango=0
                indice=''
                msg=''
                i=0
		pad=0

        #obtener el nombre de usuario
        u=User.objects.get(username=request.user.username)
        #obtener los edificios que tiene esos codigos
        e=edificio.objects.filter(user=u)
        variables_informe=dict()
        variables_informe['current']=e[0]

        var=[0,1,2,3,4,5,6,7,8,9]
        var_col=['00FF03','50F000','80E501','95E500','CFE500','FFFF00','FFE000','FFCA01','FF8000','FB0200']
        var_ind=[u'A1',u'A2',u'B1',u'B2',u'C1',u'C2',u'D',u'E',u'F',u'G']
        var_ran=[u'25',u'50',u'75',u'100',u'125',u'175',u'225',u'300',u'380',u'450']
        ratings=list()
        for i in var:
                temp=rate()
                temp.color=var_col[i]
                temp.rango=var_ran[i]
                temp.indice=var_ind[i]
                temp.i=(i+1)*3
                if var_ran[i]==variables_informe['current'].rating_potencial:
                        temp.msg='Indice Potencial: '
			temp.pad="6"
                if var_ran[i]==variables_informe['current'].rating_actual:
                        temp.msg='Indice Actual: '
                ratings.append(temp)

        variables_informe['tabs']=tabs(request)
        variables_informe['edificios']=e
        variables_informe['ratings']=ratings
	return variables_informe


def get_score(request):
	variables_informe=head(request)
        return ["scorecard.html",variables_informe]

def get_info(request):
	variables_informe=head(request)
	return ["informe.html",variables_informe]

def graficos(request,tipo):
        values={'t':'totales.png','a':'a.png','b':'b.png','c':'c.png'}
        return open(os.getcwd() + "/templates/" + values[tipo], "rb").read()

def cuadro_consumo(request):

        #for ambiente in edificio, [ambiente,refrigeracion,calefaccion,iluminacion,otro]

        cuadro=[['Oficina principal primer piso',2,3,4,5,25],['Recepcion primer piso',6,7,8,9,25]]
        return cuadro


