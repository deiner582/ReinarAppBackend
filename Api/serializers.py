from rest_framework.serializers import ModelSerializer
from .models import Colegio,Estudiante,Puntuacion,Docente,User
class ColegioSerialerzs(ModelSerializer):
    class Meta:
        model= Colegio
        fields=('codigo','nombre','direccion','telefono','estado')

class EstudianteSerialerzs(ModelSerializer):
    class Meta:
        model= Estudiante
        fields=('documento','primer_nombre','primer_apellido','sexo','usuario','correo','colegio')

class DocenteSerialerzs(ModelSerializer):
    class Meta:
        model= Docente
        fields=('documento','primer_nombre','primer_apellido','sexo','usuario','correo','colegio')

class PuntuacionSerialerzs(ModelSerializer):
    class Meta:
        model= Puntuacion
        fields=('estudiante','puntuacion','fecha')

class UsuarioSerialerzs(ModelSerializer):
    class Meta:
        model= User
        fields = ('username','password')