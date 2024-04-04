from rest_framework import generics
from core.models import Paciente, Clinica, Medico, TipoEstudio, EstudioUltrasonido, ImagenUltrasonido, VideoUltrasonido, InformeMedico, Etiqueta, Medicion
from .serializers import PacienteSerializer, ClinicaSerializer, MedicoSerializer, TipoEstudioSerializer, EstudioUltrasonidoSerializer, ImagenUltrasonidoSerializer, VideoUltrasonidoSerializer, InformeMedicoSerializer, EtiquetaSerializer, MedicionSerializer

class PacienteListAPIView(generics.ListAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idPaciente"
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteCreateAPIView(generics.CreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idPaciente"
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class PacienteDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idPaciente"
    queryset = Paciente.objects.all()
    
    
# Vistas para el modelo Clinica
class ClinicaListAPIView(generics.ListAPIView):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer

class ClinicaDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idClinica"
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer

class ClinicaCreateAPIView(generics.CreateAPIView):
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer

class ClinicaUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idClinica"
    queryset = Clinica.objects.all()
    serializer_class = ClinicaSerializer

class ClinicaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idClinica"
    queryset = Clinica.objects.all()


class MedicoListAPIView(generics.ListAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idMedico"
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoCreateAPIView(generics.CreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idMedico"
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

class MedicoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idMedico"
    queryset = Medico.objects.all()
    

class TipoEstudioListAPIView(generics.ListAPIView):
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class TipoEstudioDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idTipoEstudio"
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class TipoEstudioCreateAPIView(generics.CreateAPIView):
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class TipoEstudioUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idTipoEstudio"
    queryset = TipoEstudio.objects.all()
    serializer_class = TipoEstudioSerializer

class TipoEstudioDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idTipoEstudio"
    queryset = TipoEstudio.objects.all()
    

class EstudioUltrasonidoListAPIView(generics.ListAPIView):
    queryset = EstudioUltrasonido.objects.all()
    serializer_class = EstudioUltrasonidoSerializer

class EstudioUltrasonidoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idEstudioUltrasonido"
    queryset = EstudioUltrasonido.objects.all()
    serializer_class = EstudioUltrasonidoSerializer

class EstudioUltrasonidoCreateAPIView(generics.CreateAPIView):
    queryset = EstudioUltrasonido.objects.all()
    serializer_class = EstudioUltrasonidoSerializer

class EstudioUltrasonidoUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idEstudioUltrasonido"
    queryset = EstudioUltrasonido.objects.all()
    serializer_class = EstudioUltrasonidoSerializer

class EstudioUltrasonidoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idEstudioUltrasonido"
    queryset = EstudioUltrasonido.objects.all()



class ImagenUltrasonidoListAPIView(generics.ListAPIView):
    queryset = ImagenUltrasonido.objects.all()
    serializer_class = ImagenUltrasonidoSerializer

class ImagenUltrasonidoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idImagenUltrasonido"
    queryset = ImagenUltrasonido.objects.all()
    serializer_class = ImagenUltrasonidoSerializer

class ImagenUltrasonidoCreateAPIView(generics.CreateAPIView):
    queryset = ImagenUltrasonido.objects.all()
    serializer_class = ImagenUltrasonidoSerializer

class ImagenUltrasonidoUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idImagenUltrasonido"
    queryset = ImagenUltrasonido.objects.all()
    serializer_class = ImagenUltrasonidoSerializer

class ImagenUltrasonidoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idImagenUltrasonido"
    queryset = ImagenUltrasonido.objects.all()
    



class VideoUltrasonidoListAPIView(generics.ListAPIView):
    queryset = VideoUltrasonido.objects.all()
    serializer_class = VideoUltrasonidoSerializer

class VideoUltrasonidoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idVideoUltrasonido"
    queryset = VideoUltrasonido.objects.all()
    serializer_class = VideoUltrasonidoSerializer

class VideoUltrasonidoCreateAPIView(generics.CreateAPIView):
    queryset = VideoUltrasonido.objects.all()
    serializer_class = VideoUltrasonidoSerializer

class VideoUltrasonidoUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idVideoUltrasonido"
    queryset = VideoUltrasonido.objects.all()
    serializer_class = VideoUltrasonidoSerializer

class VideoUltrasonidoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idVideoUltrasonido"
    queryset = VideoUltrasonido.objects.all()



# Vistas para InformeMedico
class InformeMedicoListAPIView(generics.ListAPIView):
    queryset = InformeMedico.objects.all()
    serializer_class = InformeMedicoSerializer

class InformeMedicoDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idInformeMedico"
    queryset = InformeMedico.objects.all()
    serializer_class = InformeMedicoSerializer

class InformeMedicoCreateAPIView(generics.CreateAPIView):
    queryset = InformeMedico.objects.all()
    serializer_class = InformeMedicoSerializer

class InformeMedicoUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idInformeMedico"
    queryset = InformeMedico.objects.all()
    serializer_class = InformeMedicoSerializer

class InformeMedicoDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idInformeMedico"
    queryset = InformeMedico.objects.all()

# Vistas para Etiqueta
class EtiquetaListAPIView(generics.ListAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EtiquetaDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idEtiqueta"
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EtiquetaCreateAPIView(generics.CreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EtiquetaUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idEtiqueta"
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EtiquetaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idEtiqueta"
    queryset = Etiqueta.objects.all()

# Vistas para Medicion
class MedicionListAPIView(generics.ListAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class MedicionDetailAPIView(generics.RetrieveAPIView):
    lookup_field = "idMedicion"
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class MedicionCreateAPIView(generics.CreateAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class MedicionUpdateAPIView(generics.UpdateAPIView):
    lookup_field = "idMedicion"
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

class MedicionDestroyAPIView(generics.DestroyAPIView):
    lookup_field = "idMedicion"
    queryset = Medicion.objects.all()