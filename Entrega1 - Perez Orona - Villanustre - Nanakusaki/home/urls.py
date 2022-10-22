from django.urls import path
from home import views

urlpatterns = [
    path('hola/', views.hola, name= 'hola'),
    path('fecha/', views.fecha, name= 'fecha'),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('mi-template/',views.mi_template),
    path('mi-template/<str:nombre>',views.tu_template),
    path('prueba-template/',views.prueba_template),
    path('ver-personas/',views.ver_persona, name= 'ver_persona'),
    path('crear-persona/',views.crear_persona, name= 'crear_persona'),
    path('',views.index, name= 'index'),
  ]