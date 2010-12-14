#!bin/sh

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from generators import *
from django.shortcuts import render_to_response
import os

#librerias graficas
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import mpl
import numpy as np
##############

@login_required
def account (request,sel):
	c={}
	c.update(csrf(request))
	response=body(request,sel)
        return render_to_response(response[0],response[1])

def general(request):
        c = {}
        c.update(csrf(request))
	dict=tabs(request)
	dict['col1']='General'
	return render_to_response("template.html",dict)

def formato(request,tipo):
	c = {}
	c.update(csrf(request))
	if tipo == 'screen':
		response=open(os.getcwd() + "/templates/screen.css", "rb").read()
	if tipo == 'head':
		response=open(os.getcwd() + "/templates/negro.png", "rb").read()
	return HttpResponse(response,c) 

def contacto(request):
        c = {}
        c.update(csrf(request))
        dict=tabs(request)
	errors = []
	if request.method == 'POST':
		if not request.POST.get('subject', ''):
			errors.append('Enter a subject.')
	if not request.POST.get('message', ''):
		errors.append('Enter a message.')
	if request.POST.get('email') and '@' not in request.POST['email']:
		errors.append('Enter a valid e-mail address.')
	if not errors:
		#send_mail(request.POST['subject'],request.POST['message'],request.POST.get('email', 'noreply@example.com'),['siteowner@example.com'],)
		return HttpResponseRedirect('/contact/thanks/')
	return render_to_response('contacto.html', {'errors': errors,'subject': request.POST.get('subject', ''),'message': request.POST.get('message', ''),'email': request.POST.get('email', ''),})


def score(request):
        c = {}
        c.update(csrf(request))
        dict=tabs(request)
        dict['col1']='General'
        return render_to_response("template.html",dict)


############################################################################################################################3
def graficos(request,sel):
	opt={'score.png':score,'d_anual.png':d_anual,'mensual.png':mensual,'end_use.png':end_use}
	return opt.get(sel)(request)

def end_use(request):
        N=12
        ind = np.arange(N)  # the x locations for the groups
        width=0.35
        fig=Figure(figsize=(9,5),facecolor='w', edgecolor='w')

        ax=fig.add_subplot(221)
        actual=[9,9,6,3,1,0,0,0,1,2,6,9]
        ax.bar(ind,actual,0.35,alpha=1,color='b')
        ax.set_xticks(ind+width)
        ax.set_xticklabels(('E','F','M','A','M','J','J','A','S','O','N','D'))

        ax=fig.add_subplot(222)
        actual=[0,0,0,0,2,3,6,6,3,2,1,0]
        ax.bar(ind,actual,0.35,alpha=1,color='r')
        ax.set_xticks(ind+width)
        ax.set_xticklabels(('E','F','M','A','M','J','J','A','S','O','N','D'))

        ax=fig.add_subplot(223)
        actual=[4,4,5,5,6,6,7,6,5,4,4,4]
        ax.bar(ind,actual,0.35,alpha=1,color='y')
        ax.set_xticks(ind+width)
        ax.set_xticklabels(('E','F','M','A','M','J','J','A','S','O','N','D'))

        ax=fig.add_subplot(224)
        actual=[2,3,2,3,3,3,3,3,2,3,2,2]
        ax.bar(ind,actual,0.35,alpha=1,color='m')
        ax.set_xticks(ind+width)
        ax.set_xticklabels(('E','F','M','A','M','J','J','A','S','O','N','D'))


        canvas=FigureCanvas(fig)
        response=HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response



def mensual(request):
	N=12
	ind = np.arange(N)  # the x locations for the groups
	width=0.3
	fig=Figure(figsize=(8,3),facecolor='w', edgecolor='w')
	ax=fig.add_subplot(111)
	actual=[5,5,7,6,5,7,6,6,7,6,5,5]
	green=[4,4,5,4,5,5,3,4,3,4,5,4]
	ax.bar(ind,actual,width,alpha=1,color='red')
	ax.bar(ind+width,green,width,alpha=0.8,color='green')
	ax.set_xticks(ind+width)
	ax.set_xticklabels(('Ene','Feb','Mar','Abr','May','Jun','Jul','Ago','Sep','Oct','Nov','Dic'))
	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response



def d_anual(request):
        fig = Figure(figsize=(8, 1), facecolor='w', edgecolor='w')
        canvas = FigureCanvas(fig)
        ax = fig.add_axes([0.05, 0.5, 0.9, 0.35]) #Coordenadas del grafico [left,bottom, width, height]

	cmap = mpl.colors.ListedColormap(['b', 'r', 'y', 'm'])
	#cmap.set_over('0.25')
	#cmap.set_under('0.75')
	bounds = [1, 2, 4, 7, 8]
	t_bounds = [0+(2.0)/2.0,2+(4.0-2)/2,4+(7.0-4)/2,7+(10.0-7)/2.0]

	norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
	cb2 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,boundaries=[0]+bounds+[10],norm=norm,ticks=t_bounds, spacing='proportional',orientation='horizontal')
	#cb2.set_label('Discrete intervals, some other units')
        cb2.ax.set_xticklabels(['R','C','I','O'])
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response

def score(request):
	fig = Figure(figsize=(8, 1), facecolor='w', edgecolor='w')
	canvas = FigureCanvas(fig)
	ax = fig.add_axes([0.05, 0.5, 0.9, 0.35]) #Coordenadas del grafico [left,bottom, width, height]
	cmap = mpl.cm.RdYlGn
	norm = mpl.colors.Normalize(vmin=0, vmax=10)
	cb1 = mpl.colorbar.ColorbarBase(ax, cmap=cmap,norm=norm,orientation='horizontal',ticks=(0,5,7,10))
	cb1.ax.set_xticklabels(['Minima','Actual','Potencial','Maxima'])
	response = HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
