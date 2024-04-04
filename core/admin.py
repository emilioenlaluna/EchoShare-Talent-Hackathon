
from django.contrib import admin
from .models import Paciente, Clinica, Medico, CitaMedica,TipoEstudio, EstudioUltrasonido, ImagenUltrasonido, VideoUltrasonido, InformeMedico, Etiqueta, Medicion


from django.contrib import admin
from .forms import PacienteForm


    
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('idPaciente', 'Nombre', 'Apellido', 'Correo', 'FechaNacimiento', 'Sexo')
    list_filter = ('Sexo',)
    search_fields = ('Nombre', 'Apellido', 'Correo')
    form = PacienteForm

class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('idClinica', 'Nombre', 'Ciudad', 'Telefono', 'Correo')
    search_fields = ('Nombre', 'Ciudad')

class MedicoAdmin(admin.ModelAdmin):
    list_display = ('idMedico', 'Nombre', 'Apellido', 'Especialidad', 'Telefono', 'Correo')
    search_fields = ('Nombre', 'Apellido', 'Especialidad')

class TipoEstudioAdmin(admin.ModelAdmin):
    list_display = ('idTipoEstudio', 'Nombre', 'Descripcion', 'Duracion', 'Costo')
    search_fields = ('Nombre', 'Descripcion')
    list_filter = ('Descripcion', 'Duracion', 'Costo')
    #list_editable = ('Descripcion', 'Duracion', 'Costo')

class CitaMedicaAdmin(admin.ModelAdmin):
    list_display = ('idCitaMedica', 'Fecha', 'Hora','Observaciones')
    list_filter = ('Fecha','Observaciones')
    search_fields = ('idCitaMedica', 'Fecha', 'Hora','Observaciones')


class EstudioUltrasonidoAdmin(admin.ModelAdmin):
    list_display = ('idEstudioUltrasonido', 'Paciente', 'Clinica', 'Medico', 'TipoEstudio', 'Fecha', 'Hora')
    list_filter = ('Clinica', 'Medico', 'Fecha')
    search_fields = ('Paciente__Nombre', 'Paciente__Apellido', 'Clinica__Nombre', 'Medico__Nombre')

class ImagenUltrasonidoAdmin(admin.ModelAdmin):
    list_display = ('idImagenUltrasonido', 'Imagen', 'EstudioUltrasonido', 'Tipo', 'Fecha', 'Notas', 'Calificacion')
    list_filter = ('Tipo', 'Fecha')
    search_fields = ('EstudioUltrasonido__Paciente__Nombre', 'EstudioUltrasonido__Paciente__Apellido')

class VideoUltrasonidoAdmin(admin.ModelAdmin):
    list_display = ('idVideoUltrasonido', 'Video', 'EstudioUltrasonido', 'Fecha', 'Tipo', 'Notas', 'Calidad')
    list_filter = ('Tipo', 'Fecha')
    search_fields = ('EstudioUltrasonido__Paciente__Nombre', 'EstudioUltrasonido__Paciente__Apellido')

class InformeMedicoAdmin(admin.ModelAdmin):
    list_display = ('idInformeMedico', 'Detalles', 'EstudioUltrasonido', 'Notas', 'fecha', 'Doctor', 'Diagnostico', 'Recomendaciones')
    list_filter = ('fecha', 'Doctor')
    search_fields = ('EstudioUltrasonido__Paciente__Nombre', 'EstudioUltrasonido__Paciente__Apellido')

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = ('idEtiqueta', 'Nombre', 'Tipo', 'Descripcion', 'Coordernadas', 'Color')
    list_filter = ('Tipo', 'Color')
    search_fields = ('Nombre', 'Tipo', 'Descripcion')

class MedicionAdmin(admin.ModelAdmin):
    list_display = ('idMedicion', 'ImagenUltrasonido', 'Nombre', 'Tipo', 'Contenido', 'Valor', 'Unidad', 'RangoNormal', 'Interpretacion')
    list_filter = ('Tipo',)
    search_fields = ('Nombre', 'Tipo', 'Contenido')

# Registra los modelos con sus clases de administración personalizadas
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(TipoEstudio, TipoEstudioAdmin)
admin.site.register(EstudioUltrasonido, EstudioUltrasonidoAdmin)
admin.site.register(ImagenUltrasonido, ImagenUltrasonidoAdmin)
admin.site.register(VideoUltrasonido, VideoUltrasonidoAdmin)
admin.site.register(InformeMedico, InformeMedicoAdmin)
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Medicion, MedicionAdmin)
admin.site.register(CitaMedica, CitaMedicaAdmin)


admin.site.site_header = 'EchoShare by Salud Digna'
admin.site.site_title = 'Admin de Ultrasonidos'
admin.site.index_title = 'Bienvenido al Panel de Administración de echoshare '


