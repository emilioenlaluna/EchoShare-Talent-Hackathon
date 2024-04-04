from django import forms
from .models import Paciente
import uuid

class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.idPaciente:
            self.instance.idPaciente = uuid.uuid4()

    class Meta:
        model = Paciente
        fields = '__all__'