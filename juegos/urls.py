from django.urls import path
from.import views

urlpatterns= [
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('accion/', views.accion, name='accion'),
    path('gary_mod/', views.gary_mod, name='gary_mod'),
    path('gta/', views.gta, name='gta'),
    path('kirby/', views.kirby, name='kirby'),
    path('login/', views.login, name='login'),
    path('protegida/', views.vista_protegida, name='protegida'),
    path('minecraft/', views.minecraft, name='minecraft'),
    path('mundo_abierto/', views.mundo_abierto, name='mundo_abierto'),
    path('resident_evil/', views.resident_evil, name='resident_evil'),
    path('subnautica/', views.subnautica, name='subnautica'),
    path('supermario/', views.supermario, name='supermario'),
    path('supervivencia/', views.supervivencia, name='supervivencia'),
    path('suspenso/', views.suspenso, name='suspenso'),
    path('terror/', views.terror, name='terror'),
    path('the_evil_within/', views.the_evil_within_2, name='the_evil_within'),
    path('the_witcher/', views.the_witcher, name='the_witcher'),
    path('theforest/', views.theforest, name='theforest'),
    path('todosLosJuegos/', views.todosLosJuegos, name='todosLosJuegos'),
    path('tom_raider/', views.tom_raider, name='tom_raider'),
    path('zelda/', views.zelda, name='zelda'),
    
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear', views.crear_producto, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.editar_producto, name='listar_productos'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_productos'),
]