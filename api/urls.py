from django.urls import path
from . import views

urlpatterns = [
    # URLs para el modelo Paciente
    path('paciente/', views.PacienteListAPIView.as_view(), name='paciente_list'),
    path('paciente/<int:idPaciente>/', views.PacienteDetailAPIView.as_view(), name='paciente_detail'),
    path('paciente/create/', views.PacienteCreateAPIView.as_view(), name='paciente_create'),
    path('paciente/update/<int:idPaciente>/', views.PacienteUpdateAPIView.as_view(), name='paciente_update'),
    path('paciente/delete/<int:idPaciente>/', views.PacienteDestroyAPIView.as_view(), name='paciente_delete'),

    # URLs para el modelo Clinica
    path('clinica/', views.ClinicaListAPIView.as_view(), name='clinica_list'),
    path('clinica/<int:idClinica>/', views.ClinicaDetailAPIView.as_view(), name='clinica_detail'),
    path('clinica/create/', views.ClinicaCreateAPIView.as_view(), name='clinica_create'),
    path('clinica/update/<int:idClinica>/', views.ClinicaUpdateAPIView.as_view(), name='clinica_update'),
    path('clinica/delete/<int:idClinica>/', views.ClinicaDestroyAPIView.as_view(), name='clinica_delete'),

    # URLs para el modelo Medico
    path('medico/', views.MedicoListAPIView.as_view(), name='medico_list'),
    path('medico/<int:idMedico>/', views.MedicoDetailAPIView.as_view(), name='medico_detail'),
    path('medico/create/', views.MedicoCreateAPIView.as_view(), name='medico_create'),
    path('medico/update/<int:idMedico>/', views.MedicoUpdateAPIView.as_view(), name='medico_update'),
    path('medico/delete/<int:idMedico>/', views.MedicoDestroyAPIView.as_view(), name='medico_delete'),

    # URLs para el modelo TipoEstudio
    path('tipo-estudio/', views.TipoEstudioListAPIView.as_view(), name='tipo_estudio_list'),
    path('tipo-estudio/<int:idTipoEstudio>/', views.TipoEstudioDetailAPIView.as_view(), name='tipo_estudio_detail'),
    path('tipo-estudio/create/', views.TipoEstudioCreateAPIView.as_view(), name='tipo_estudio_create'),
    path('tipo-estudio/update/<int:idTipoEstudio>/', views.TipoEstudioUpdateAPIView.as_view(), name='tipo_estudio_update'),
    path('tipo-estudio/delete/<int:idTipoEstudio>/', views.TipoEstudioDestroyAPIView.as_view(), name='tipo_estudio_delete'),

    # URLs para el modelo EstudioUltrasonido
    path('estudio-ultrasonido/', views.EstudioUltrasonidoListAPIView.as_view(), name='estudio_ultrasonido_list'),
    path('estudio-ultrasonido/<int:idEstudioUltrasonido>/', views.EstudioUltrasonidoDetailAPIView.as_view(), name='estudio_ultrasonido_detail'),
    path('estudio-ultrasonido/create/', views.EstudioUltrasonidoCreateAPIView.as_view(), name='estudio_ultrasonido_create'),
    path('estudio-ultrasonido/update/<int:idEstudioUltrasonido>/', views.EstudioUltrasonidoUpdateAPIView.as_view(), name='estudio_ultrasonido_update'),
    path('estudio-ultrasonido/delete/<int:idEstudioUltrasonido>/', views.EstudioUltrasonidoDestroyAPIView.as_view(), name='estudio_ultrasonido_delete'),

    # URLs para el modelo ImagenUltrasonido
    path('imagen-ultrasonido/', views.ImagenUltrasonidoListAPIView.as_view(), name='imagen_ultrasonido_list'),
    path('imagen-ultrasonido/<int:idImagenUltrasonido>/', views.ImagenUltrasonidoDetailAPIView.as_view(), name='imagen_ultrasonido_detail'),
    path('imagen-ultrasonido/create/', views.ImagenUltrasonidoCreateAPIView.as_view(), name='imagen_ultrasonido_create'),
    path('imagen-ultrasonido/update/<int:idImagenUltrasonido>/', views.ImagenUltrasonidoUpdateAPIView.as_view(), name='imagen_ultrasonido_update'),
    path('imagen-ultrasonido/delete/<int:idImagenUltrasonido>/', views.ImagenUltrasonidoDestroyAPIView.as_view(), name='imagen_ultrasonido_delete'),

    # URLs para el modelo VideoUltrasonido
    path('video-ultrasonido/', views.VideoUltrasonidoListAPIView.as_view(), name='video_ultrasonido_list'),
    path('video-ultrasonido/<int:idVideoUltrasonido>/', views.VideoUltrasonidoDetailAPIView.as_view(), name='video_ultrasonido_detail'),
    path('video-ultrasonido/create/', views.VideoUltrasonidoCreateAPIView.as_view(), name='video_ultrasonido_create'),
    path('video-ultrasonido/update/<int:idVideoUltrasonido>/', views.VideoUltrasonidoUpdateAPIView.as_view(), name='video_ultrasonido_update'),
    path('video-ultrasonido/delete/<int:idVideoUltrasonido>/', views.VideoUltrasonidoDestroyAPIView.as_view(), name='video_ultrasonido_delete'),

    # URLs para el modelo InformeMedico
    path('informe-medico/', views.InformeMedicoListAPIView.as_view(), name='informe_medico_list'),
    path('informe-medico/<int:idInformeMedico>/', views.InformeMedicoDetailAPIView.as_view(), name='informe_medico_detail'),
    path('informe-medico/create/', views.InformeMedicoCreateAPIView.as_view(), name='informe_medico_create'),
    path('informe-medico/update/<int:idInformeMedico>/', views.InformeMedicoUpdateAPIView.as_view(), name='informe_medico_update'),
    path('informe-medico/delete/<int:idInformeMedico>/', views.InformeMedicoDestroyAPIView.as_view(), name='informe_medico_delete'),

    # URLs para el modelo Etiqueta
    path('etiqueta/', views.EtiquetaListAPIView.as_view(), name='etiqueta_list'),
    path('etiqueta/<int:idEtiqueta>/', views.EtiquetaDetailAPIView.as_view(), name='etiqueta_detail'),
    path('etiqueta/create/', views.EtiquetaCreateAPIView.as_view(), name='etiqueta_create'),
    path('etiqueta/update/<int:idEtiqueta>/', views.EtiquetaUpdateAPIView.as_view(), name='etiqueta_update'),
    path('etiqueta/delete/<int:idEtiqueta>/', views.EtiquetaDestroyAPIView.as_view(), name='etiqueta_delete'),

    # URLs para el modelo Medicion
    path('medicion/', views.MedicionListAPIView.as_view(), name='medicion_list'),
    path('medicion/<int:idMedicion>/', views.MedicionDetailAPIView.as_view(), name='medicion_detail'),
    path('medicion/create/', views.MedicionCreateAPIView.as_view(), name='medicion_create'),
    path('medicion/update/<int:idMedicion>/', views.MedicionUpdateAPIView.as_view(), name='medicion_update'),
    path('medicion/delete/<int:idMedicion>/', views.MedicionDestroyAPIView.as_view(), name='medicion_delete'),
]