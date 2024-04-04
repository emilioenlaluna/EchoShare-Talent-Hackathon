from rest_framework import serializers
from core.models import Paciente, Clinica, Medico, TipoEstudio, EstudioUltrasonido, ImagenUltrasonido, VideoUltrasonido, InformeMedico, Etiqueta, Medicion

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('idPaciente', 'Nombre', 'Apellido', 'Telefono', 'Correo', 'FechaNacimiento', 'Sexo', 'Direccion', 'Ciudad', 'Estado', 'Pais')

class ClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinica
        fields = ('idClinica', 'Nombre', 'Codigo', 'Domicilio', 'Cp', 'Ciudad', 'Telefono', 'Fax', 'Correo', 'SitioWeb')

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('idMedico', 'Nombre', 'Apellido', 'Especialidad', 'Cedula', 'Telefono', 'Correo')

class TipoEstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstudio
        fields = ('idTipoEstudio', 'Nombre', 'Descripcion', 'Imagen', 'Duracion', 'Codigo', 'Costo', 'Observaciones')

class EstudioUltrasonidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstudioUltrasonido
        fields = ('idEstudioUltrasonido', 'Paciente', 'Clinica', 'Medico', 'TipoEstudio', 'Fecha', 'Hora', 'Observaciones')

class ImagenUltrasonidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenUltrasonido
        fields = ('idImagenUltrasonido', 'Imagen', 'EstudioUltrasonido', 'Tipo', 'Fecha', 'Notas', 'Calificacion')

class VideoUltrasonidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoUltrasonido
        fields = ('idVideoUltrasonido', 'Video', 'EstudioUltrasonido', 'Fecha', 'Tipo', 'Notas', 'Calidad')

class InformeMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformeMedico
        fields = ('idInformeMedico', 'Detalles', 'EstudioUltrasonido', 'Notas', 'fecha', 'Doctor', 'Diagnostico', 'Recomendaciones')

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = ('idEtiqueta', 'ImagenUltrasonido', 'Nombre', 'Tipo', 'Descripcion', 'Coordernadas', 'Color')

class MedicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicion
        fields = ('idMedicion', 'ImagenUltrasonido', 'Nombre', 'Tipo', 'Contenido', 'Valor', 'Unidad', 'RangoNormal', 'Interpretacion')