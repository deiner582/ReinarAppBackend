from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ColegioSerialerzs,EstudianteSerialerzs,DocenteSerialerzs,PuntuacionSerialerzs
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
class ColegioApi(APIView):
    serializer_class = ColegioSerialerzs
    def get(self,request,cod=None,format=None):
        muchos = False
        if cod != None:
            colegio = get_object_or_404(Colegio,pk=cod)
        else:
            muchos = True
            colegio = Colegio.objects.all()
        response = self.serializer_class(colegio,many=muchos)
        return Response(response.data)

class EstudianteApi(APIView):
    serializer_class = EstudianteSerialerzs
    def get(self,request,ced=None,format=None):
        muchos = False
        if ced != None:
            estudiante = get_object_or_404(Estudiante,pk=ced)
        else:
            muchos = True
            estudiante= Estudiante.objects.all()
        response=self.serializer_class(estudiante,many=muchos)
        return Response(response.data)

class DocenteApi(APIView):
    serializer_class = DocenteSerialerzs
    def get(self,request,ced=None,format=None):
        muchos = False
        if ced != None:
            docente=get_object_or_404(Docente,pk=ced)
        else:
            muchos = True
            docente= Docente.objects.all()
        response = self.serializer_class(docente,many=muchos)
        return Response(response.data)


class PuntuacionApi(APIView):
    serializer_class= PuntuacionSerialerzs
    def get(self,request,cod=None,format=None):
        muchos = False
        if cod != None:
            puntuacion= get_object_or_404(Puntuacion,pk=cod)
        else:
            muchos = True
            puntuacion= Puntuacion.objects.all()
        response=self.serializer_class(puntuacion,many=muchos)
        return Response(response.data)
