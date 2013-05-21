from django.db import models

# Create your models here.

class cliente(models.Model):
	     nombre         =  models.CharField(max_length=200)
	     apellidos      =  models.CharField(max_length=200)
	     status         =  models.BooleanField(default=True)

	     def __unicode__(self):
      	        nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
      	        return nombreCompleto
      	        #retornamo la concateracion del nombre y el apellodo para mostrar mas detallado el panel

   #segunda clase para producto


class producto(models.Model):
	      nombre        = models.CharField(max_length=200)
	      descripcion   = models.TextField(max_length=300)
	      status        = models.BooleanField(default=True)

	      #retornamo el nombre del producto
	      def __unicode__(self):
	      	    return self.nombre

