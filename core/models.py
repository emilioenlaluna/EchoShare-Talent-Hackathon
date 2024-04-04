from django.db import models
from django.contrib.auth.models import User
import uuid

class Paciente(models.Model):
    idPaciente=models.UUIDField(primary_key=True, default=uuid.uuid4)
    Username = models.CharField(max_length=45, null=True)
    Password = models.CharField(max_length=255)
    Nombre = models.CharField(max_length=45, null=True)
    Apellido = models.CharField(max_length=45, null=True)
    Telefono = models.CharField(max_length=45, null=True)
    Correo = models.EmailField(max_length=45, null=True)
    FechaNacimiento = models.DateField(null=True)
    Sexo = models.CharField(max_length=1, null=True)
    Direccion = models.CharField(max_length=100, null=True)
    Ciudad = models.CharField(max_length=45, null=True)
    Estado = models.CharField(max_length=45, null=True)
    Pais = models.CharField(max_length=45, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'
    
class MensajeWhatsApp(models.Model):
    idMensaje = models.UUIDField(primary_key=True, default=uuid.uuid4)
    destinatario = models.CharField(max_length=20)  # Número de teléfono del destinatario
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE,null=True)
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)
    enviado = models.BooleanField(default=False)  # Para rastrear si el mensaje fue enviado correctamente

    def __str__(self):
        return f'Mensaje a {self.destinatario} - Enviado: {self.enviado}'

class RespuestaBot(models.Model):
    idRespuesta = models.UUIDField(primary_key=True, default=uuid.uuid4)
    mensaje_original = models.ForeignKey(MensajeWhatsApp, on_delete=models.CASCADE)
    contenido_respuesta = models.TextField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)


class Clinica(models.Model):
    idClinica =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Nombre = models.CharField(max_length=45, null=True)
    Codigo = models.CharField(max_length=45, null=True)
    Domicilio = models.CharField(max_length=45, null=True)
    Cp = models.CharField(max_length=45, null=True)
    Ciudad = models.CharField(max_length=45, null=True)
    Telefono = models.CharField(max_length=45, null=True)
    Fax = models.CharField(max_length=45, null=True)
    Correo = models.EmailField(max_length=45, null=True)
    SitioWeb = models.URLField(max_length=200, null=True)
    
    def __str__(self):
        return self.Nombre

class Medico(models.Model):
    idMedico =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Nombre = models.CharField(max_length=45, null=True)
    Apellido = models.CharField(max_length=45, null=True)
    Especialidad = models.CharField(max_length=45, null=True)
    Cedula = models.CharField(max_length=45, null=True)
    Telefono = models.CharField(max_length=45, null=True)
    Correo = models.EmailField(max_length=45, null=True)
    
    def __str__(self):
        return f'{self.Nombre} {self.Apellido}'

class TipoEstudio(models.Model):
    idTipoEstudio =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Nombre = models.CharField(max_length=45, null=True)
    Descripcion = models.TextField(null=True)
    Imagen = models.ImageField(upload_to='tipo_estudio/', null=True)
    Duracion = models.FloatField(null=True)
    Codigo = models.CharField(max_length=45, null=True)
    Costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    Observaciones = models.TextField(null=True)
    
    def __str__(self):
        return self.Nombre
    
class CitaMedica(models.Model):
    idCitaMedica =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Fecha = models.DateField(null=True)
    Hora = models.TimeField(null=True)
    Observaciones = models.TextField(null=True)
    
    def __str__(self):
        return f'Estudio de Ultrasonido para {self.idCitaMedica}'

class EstudioUltrasonido(models.Model):
    idEstudioUltrasonido =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    Clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE)
    Medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    TipoEstudio = models.ForeignKey(TipoEstudio, on_delete=models.CASCADE)
    CitaMedica = models.ForeignKey(CitaMedica, on_delete=models.CASCADE,null=True)
    Fecha = models.DateField(null=True)
    Hora = models.TimeField(null=True)
    Observaciones = models.TextField(null=True)
    
    def __str__(self):
        return f'Estudio de Ultrasonido para {self.Paciente}'

class ImagenUltrasonido(models.Model):
    idImagenUltrasonido =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Imagen = models.ImageField(upload_to='imagenes/', null=True)
    EstudioUltrasonido = models.ForeignKey(EstudioUltrasonido, on_delete=models.CASCADE)
    Tipo = models.CharField(max_length=45, null=True)
    Fecha = models.DateTimeField(null=True)
    Notas = models.CharField(max_length=255, null=True)
    Calificacion = models.PositiveSmallIntegerField(null=True)
    
    def __str__(self):
        return f'Imagen de Ultrasonido para {self.EstudioUltrasonido.Paciente}'

class VideoUltrasonido(models.Model):
    idVideoUltrasonido = models.UUIDField(primary_key=True, default=uuid.uuid4)
    Video = models.FileField(upload_to='videos/', null=True)
    EstudioUltrasonido = models.ForeignKey(EstudioUltrasonido, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(null=True)
    Tipo = models.CharField(max_length=45, null=True)
    Notas = models.CharField(max_length=255, null=True)
    Calidad = models.CharField(max_length=45, null=True)
    
    def __str__(self):
        return f'Video de Ultrasonido para {self.EstudioUltrasonido.Paciente}'

class InformeMedico(models.Model):
    idInformeMedico =  models.UUIDField(primary_key=True, default=uuid.uuid4)
    Detalles = models.TextField(null=True)
    EstudioUltrasonido = models.ForeignKey(EstudioUltrasonido, on_delete=models.CASCADE)
    Notas = models.CharField(max_length=255, null=True)
    fecha = models.DateField(null=True)
    Doctor = models.CharField(max_length=45, null=True)
    Diagnostico = models.TextField(null=True)
    Recomendaciones = models.TextField(null=True)
    
    def __str__(self):
        return f'Informe Médico para {self.EstudioUltrasonido.Paciente}'

class Etiqueta(models.Model):
    idEtiqueta = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ImagenUltrasonido = models.ForeignKey(ImagenUltrasonido, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=45, null=True)
    Tipo = models.CharField(max_length=45, null=True)
    Descripcion = models.CharField(max_length=255, null=True)
    Coordernadas = models.CharField(max_length=100, null=True)
    Color = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.Nombre

class Medicion(models.Model):
    idMedicion = models.UUIDField(primary_key=True, default=uuid.uuid4)
    ImagenUltrasonido = models.ForeignKey(ImagenUltrasonido, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=45, null=True)
    Tipo = models.CharField(max_length=45, null=True)
    Contenido = models.TextField(null=True)
    Valor = models.FloatField(null=True)
    Unidad = models.CharField(max_length=45, null=True)
    RangoNormal = models.CharField(max_length=45, null=True)
    Interpretacion = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return f'Medición de {self.Nombre} para {self.ImagenUltrasonido.EstudioUltrasonido.Paciente}'



    



