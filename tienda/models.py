from sys import maxsize
from django.db import models


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de la categoria")
    nombreCategoria = models.CharField(max_length=40 , verbose_name="Nombre de la categoria")
    
    def __str__(self):
        return self.nombreCategoria


class Mascota(models.Model):
    idProductomascota= models.IntegerField(primary_key=True, verbose_name="Id del producto")
    PrecioProducto = models.IntegerField(verbose_name="Precio del producto", default=999999)
    nombreProducto = models.CharField(max_length=70, verbose_name="Nombre del producto")
    SexoProducto = models.CharField(max_length=1, verbose_name="Sexo de la mascota")
    cantidadProducto = models.IntegerField(verbose_name="Cantidad de productos") 
    fechaProducto = models.DateField( verbose_name="Fecha del producto")
    DescripcionProducto = models.CharField(max_length=306, verbose_name="Descripcion del producto", default="Escriba aqui")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    
    def __str__(self):
        return 'id del producto: %s | el nombre del producto: %s | el sexo de la mascota: %s | la cantidad de productos: %s | la fecha del producto: %s | descripcion del producto: %s| el nombre categoria: %s | ' % (self.idProductomascota, self.nombreProducto, self.SexoProducto, self.cantidadProducto, self.fechaProducto, self.DescripcionProducto, self.categoria)
