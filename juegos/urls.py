from django.urls import path
from.import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView


urlpatterns= [
    path('index/', views.home, name='home'),
    path('', views.index, name='index'),
    path('registro/', views.registro, name='registro'),
    path('accion/', views.accion, name='accion'),
    path('gary_mod/', views.gary_mod, name='gary_mod'),
    path('gta/', views.gta, name='gta'),
    path('kirby/', views.kirby, name='kirby'),
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
    path('productos/editar/<int:pk>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),

    path('login/', CustomLoginView.as_view(), name='login'), #aqui usamos la vista personalizada
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='juegos/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='juegos/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='juegos/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='juegos/password_reset_complete.html'), name='password_reset_complete'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/vaciar/', views.vaciar_carrito, name='vaciar_carrito'),
    path('carrito/actualizar/<int:producto_id>/', views.actualizar_cantidad_carrito, name='actualizar_cantidad_carrito'),
    path('api/productos/', views.productos_api, name='productos_api'),
    path('categorias-juegos/', views.listar_categorias_juegos, name='listar_categorias_juegos')
]


