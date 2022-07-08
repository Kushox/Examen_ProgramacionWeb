from django.contrib import admin
from django.urls import path, include
from tienda import views
from django.contrib.auth.views import LoginView

from tienda.views import MascotaViewset, CategoriaViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mascota', MascotaViewset)
router.register('categoria', CategoriaViewset)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('gato/', views.gato, name='gato'),
    path('perro/', views.perro, name='perro'),
    path('quienesomos/', views.quienesomos, name='quienesomos'),
    path('productos/', views.productos, name='productos'),
    path('formularioag/', views.formularioag, name='formularioag'),
    path('formularioed/<id>/', views.formularioed, name='formularioed'),
    path('formularioel/<id>/', views.formularioel, name='formularioel'),
    path('carrito_compra', views.carrito_compra, name='carrito_compra'),
    path('api/', include(router.urls)),
    
   
]
