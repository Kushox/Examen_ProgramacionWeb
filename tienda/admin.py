from django.contrib import admin
from tienda.models import Categoria, Mascota

class ProductosAdmin(admin.ModelAdmin):
  
    list_display=("idProductomascota",
                  "PrecioProducto",
                  "nombreProducto",
                  "SexoProducto",
                  "cantidadProducto",
                  "fechaProducto",
                  "DescripcionProducto",
                  "categoria")
   

admin.site.register(Categoria)
admin.site.register(Mascota, ProductosAdmin)