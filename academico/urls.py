from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('registrar-curso/', views.registrar_curso),
    path('editar-curso/<codigo>', views.editar_curso),
    path('patch-curso/', views.patch_curso),
    path('eliminar-curso/<codigo>', views.eliminar_curso),
]
