# Create your views here.

from django.shortcuts import render_to_response
from django.template  import RequestContext
#importar formulario
from demo.apps.ventas.forms import addProductForm
#importar de models la clase producto
from demo.apps.ventas.models import producto

def add_product_view(request):

	if request.method == "POST":
		    form = addProductForm(request.POST)
		    info = "Inicializando"
		    if form.is_valid():
		    	   nombre = form.cleaned_data['nombre']
		    	   descripcion = form.cleaned_data['descripcion']
		    	   p = producto()
		    	   p.nombre = nombre
		    	   p.descripcion = descripcion
		    	   p.status = True
		    	   p.save() #guardar los datos
		    	   info = "Se guardaron los datos sin problemas"
		    else:

	       	                info = "Informacion con datos incorrecto"
	       	    form = addProductForm()
	       	    ctx = {'form':form, 'informacion':info}
	       	    return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
        else: # si solo es GEt muestra el form vacio
		    form = addProductForm()
		    ctx = {'form':form}
		    return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))
