from django.db import models
from django.contrib.auth.models import User


class cliente(models.Model):
	user=models.ForeignKey(User, unique=True) #link a la estructura de validacion de usuario
	codigo=models.CharField(max_length=5,primary_key=True)
	raz_social=models.CharField(max_length=30)
	cuit=models.CharField(max_length=12)
	
	def __unicode__(self):
	        return self.codigo

class edificio(models.Model):
	user=models.ForeignKey(User, unique=True) #link a la estructura de validacion de usuario
        codigo=models.ForeignKey(cliente,primary_key=True)
        nombre_edif=models.CharField(max_length=30)
        pais=models.CharField(max_length=30)
        ciudad=models.CharField(max_length=30)
        latitud=models.FloatField()
        longitd=models.FloatField()
        altitud=models.FloatField()
        direccion=models.CharField(max_length=30)
        def __unicode__(self):
                return self.nombre_edif

class ambiente(models.Model):
	tipo_amb_choices=((u'O',u'Oficina'),(u'D',u'Datacenter'),(u'P',u'Pasillo'),(u'R',u'Recepcion'),(u'C',u'Cocina'),(u'S',u'Sala'),(u'd',u'Deposito'))
	masa_termica_choices=((u'G',u'Grande'),(u'M',u'Mediana'),(u'P',u'Pequena'))

        nombre_edif=models.ForeignKey(edificio)
	fecha_relev=models.DateField()						#fecha relevamiento
	nombre_amb=models.CharField(max_length=30)				#nombre del ambiente, descriptivo
	piso=models.PositiveSmallIntegerField()					#piso en el que se encuentra el ambiente
	tipo_amb=models.CharField(max_length=10,choices=tipo_amb_choices)	#tipo de ambiente
	largo_amb=models.FloatField()
	ancho_amb=models.FloatField()
	alto_amb=models.FloatField()
	masa_termica_techo=models.CharField(max_length=1,choices=masa_termica_choices)
	masa_termica_piso=models.CharField(max_length=1,choices=masa_termica_choices)
	temp_max_ac=models.FloatField()
	temp_min_ac=models.FloatField()
	hora_inicio_semana=models.TimeField()
	hora_fin_semana=models.TimeField()
	hora_inicio_sabado=models.TimeField()
	hora_fin=models.TimeField()
	hora_inicio_domingo=models.TimeField()
	hora_fin_domingo=models.TimeField()
	personal_permanente=models.PositiveSmallIntegerField()
	def __unicode__(self):
		return self.nombre_amb

class pared(models.Model):
	orientacion_choices=((u'N',u'Norte'),(u'S',u'Sur'),(u'E',u'Este'),(u'O',u'Oeste'))
	exterior_choices=((u'A',u'Intemperie, alta exposicion'),(u'B',u'Intemperie, baja exposicion'),(u'I',u'Interior'))
	tipo_vidrio_choices=((u's',u'Vidrio simple sin aislar'),(u's',u'Vidrio simple aislado'),(u'D','DVH')) 
	tipo_abertura_choices=((u'a',u'Interna, alta perdida'),(u'b',u'Interna, baja perdida'),(u'A',u'Externa, alta perdida'),(u'B',u'Externa, baja perdida'))


	ambiente_pared=models.ForeignKey(ambiente)
	orientacion_pared=models.CharField(max_length=1,choices=orientacion_choices)
	area_pared=models.FloatField()
	r_pared=models.FloatField()
	exterior=models.CharField(max_length=1,choices=exterior_choices)
	area_vidrio=models.FloatField()
	tipo_vidrio=models.CharField(max_length=1,choices=tipo_vidrio_choices)
	r_vidrio=models.FloatField()
	area_abertura=models.FloatField()
	tipo_abertura=models.CharField(max_length=1,choices=tipo_abertura_choices)
        def __unicode__(self):
                return self.orientacion_pared


class artefacto(models.Model):
	tipo_artefacto_choices=((u'B',u'Bajo consumo'),(u'T',u'Tubo de luz'),(u'D',u'Dicroica'),(u'I','Incandescente'),(u'C',u'Computadora'),(u'i',u'Impresora'),(u'P',u'Proyector'),(u'H',u'Heladera'),(u'a',u'Cocina electrica'),(u'E',u'Estufa electrica'),(u'O',u'Otro'))
	ciclo_activo_choices=((u'E',u'Siempre activo'),(u'L',u'Activo horario laboral'),(u'S',u'Activo semi-optimo'),(u'O',u'Activo optimo'),(u'N',u'Activo horario NO laboral'))

	ambiente_artefacto=models.ForeignKey(ambiente)
	tipo_artefacto=models.CharField(max_length=1,choices=tipo_artefacto_choices)
	potencia_activo=models.FloatField()
        potencia_stand_by=models.FloatField()
	ciclo_activo=models.CharField(max_length=1,choices=ciclo_activo_choices)	
	temp_funcionamiento=models.FloatField()
        def __unicode__(self):
                return self.tipo_artefacto


class contacto(models.Model):
        codigo=models.ForeignKey(cliente,primary_key=True)
	nombre_edif=models.ForeignKey(edificio)	
	nombre_pers=models.CharField(max_length=30)
	telefono=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	cargo=models.CharField(max_length=20)
        def __unicode__(self):
                return self.nombre_pers

