from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   
   
   #############################
   #########CLIENTES##########
   #############################
   
   path('clientes/', views.listado_clientes, name='listado_clientes'),
   path('clientes/crear/', views.crear_cliente, name='crear_cliente'),
   path('clientes/editar/<int:id_cliente>/', views.editar_cliente, name='editar_cliente'),
   path('clientes/actualizar/<int:id_cliente>/', views.actualizar_cliente, name='actualizar_cliente'),
   path('clientes/eliminar/<int:id_cliente>/', views.eliminar_cliente, name='eliminar_cliente'),
   
   
   #############################
   #########GENERO JUEGO##########
   #############################
   
   path('genero-juego/', views.listado_genero_juego, name='listado_generos_juego'),
   path('genero-juego/crear/', views.crear_genero_juego, name='crear_genero_juego'),
   path('genero-juego/editar/<int:id_genero>/', views.editar_genero_juego, name='editar_genero_juego'),
   path('genero-juego/actualizar/<int:id_genero>/', views.actualizar_genero_juego, name='actualizar_genero_juego'),
   path('genero-juego/eliminar/<int:id_genero>/', views.eliminar_genero_juego, name='eliminar_genero_juego'),
   
   
   
   path('plataforma/', views.listado_plataforma, name='listado_plataforma'),
   path('plataforma/crear/', views.crear_plataforma, name='crear_plataforma'),
   path('plataforma/editar/<int:id_plataforma>/', views.editar_plataforma, name='editar_plataforma'),
   path('plataforma/actualizar/<int:id_plataforma>/', views.actualizar_plataforma, name='actualizar_plataforma'),
   path('plataforma/eliminar/<int:id_plataforma>/', views.eliminar_plataforma, name='eliminar_plataforma'),

   
   path('juego/', views.listado_juegos, name='listado_juegos'),
   path('juego_cliente/', views.listado_juegos_cliente, name='listado_juegos_cliente'),
   path('juego/crear/', views.crear_juego, name='crear_juego'),
   path('juego/editar/<int:id_juego>/', views.editar_juego, name='editar_juego'),
   path('juego/actualizar/<int:id_juego>/', views.actualizar_juego, name='actualizar_juego'),
   path('juego/eliminar/<int:id_juego>/', views.eliminar_juego, name='eliminar_juego'),
   
   
   
path('carrito/<int:id_juego>/', views.crear_carrito, name='agregar_al_carrito'), 
path('carrito/ver_carrito/', views.ver_carrito, name='mostrar_carrito'),
path('carrito/aumentar/<int:id_juego>/', views.aumentar , name='aumentar'),
path('carrito/disminuir/<int:id_juego>/', views.disminuir , name='disminuir'),


path('carrito/confirmar/', views.confirmar_compra, name='confirmar_compra'),

path('carrito/resumen/<int:id_boleta>/', views.resumen_boleta, name='resumen_boleta'),

path('boleta/listado_boleta', views.listado_boleta, name='listado_boleta'),
]