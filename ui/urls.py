from django.urls import path

from . import views
from .views import ver_ultrasonidos

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="home"),
   
     path('crearcuenta/', views.crearcuenta,  name='crearcuenta'),
    path('cerrarsesion/', views.cerrarsesion, name='cerrarsesion'),
    path('iniciarsesion/', views.iniciarsesion, name='iniciarsesion'),
    path('autenticacion/', views.facial_login_view, name='autenticacion'),
    path('success/', views.success, name='success'),
    path('paciente/<str:id_paciente>/ultrasonidos/', ver_ultrasonidos, name='ver_ultrasonidos'),
    path('paciente/<str:id_paciente>/ultrasonidos/detalle/<str:estudio_id>/', views.detalle_ultrasonido, name='detalle_ultrasonido'),
    path('ultrasonido/<uuid:id_estudio>/', views.estudio_ultrasonido_detalle, name='estudio_ultrasonido_detalle'),
 path("dashboard", views.dashboard, name="dashboard"),
 path('video/<str:video_id>', views.mostrar_video, name='show_video'),
  path('dicom/<int:dicom_id>/', views.view_dicom, name='view_dicom'),
  
   path('webhook', views.verificar_webhook, name='verificar_webhook'),
    path('webhook', views.recibir_mensajes, name='recibir_mensajes'),
      path('compartir/', views.compartir_archivos, name='compartir'),
]