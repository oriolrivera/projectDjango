#archivo para que el admin vea nuestra 2 clases cliente, producto

#importamos la libreria de admin
from django.contrib    import admin
from demo.apps.ventas.models import cliente,producto
#importamos el archivo models con sus 2 clases


#registramos las clases
admin.site.register(cliente)
admin.site.register(producto)