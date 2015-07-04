from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Colegio(models.Model):
    Estado = (
   ('Paz y salvo', 'Paz y salvo'),
   ('Moroso', 'Moroso'),
    )
    codigo=models.CharField(primary_key=True,max_length=3)
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.IntegerField()
    estado=models.CharField(max_length=12,choices=Estado,default="Moroso")

    def __unicode__(self):
        return self.nombre

class Persona(models.Model):
    Sexo = (
   ('M', 'M'),
   ('F', 'F'),
    )
    Tipo=(('C.C','Cedula de ciudadania'),
          ('T.I','Tarjeta de identidad'),
          ('C.E','Cedula Extranjera'),
          ('Registro Civil','Registro Civil')
    )
    tipo_documento=models.CharField(choices=Tipo,max_length=20)
    documento=models.IntegerField(primary_key=True)
    primer_nombre=models.CharField(max_length=50)
    segundo_nombre=models.CharField(max_length=50,null=True)
    primer_apellido=models.CharField(max_length=50)
    segundo_apellido=models.CharField(max_length=50)
    sexo=models.CharField(max_length=1,choices=Sexo,default='M')
    fecha_nacimiento=models.DateField()
    usuario=models.ForeignKey(User,null=True,blank=True)
    correo=models.EmailField(blank=True,null=True,unique=True)
    colegio = models.ForeignKey(Colegio)

    def __unicode__(self):
        return  self.primer_nombre + " "+self.primer_apellido+" "+self.segundo_apellido

    # crear un usuario a una persona automaticamente
    def save(self, *args, **kwargs):
        nombre_usuario=self.primer_nombre[0].lower()+self.segundo_nombre[0].lower()+self.primer_apellido.lower()
        user = User(username=nombre_usuario, password=str(self.documento))
        user.is_staff = True
        user.is_superuser = False
        user.save()
        self.usuario= user
        super(Persona, self).save(*args, **kwargs)

    #eliminar el usuario asociado a la persona
    def delete(self):
         user=User.objects.get(username=self.usuario)
         user.delete()

class Estudiante(Persona):
    Grado=(
       ('1','1'),
       ('2','2'),
       ('3','3'),
       ('4','4'),
       ('5','5'),
    )
    grado=models.CharField(max_length=1,choices=Grado,default='1')

class Puntuacion(models.Model):
    estudiante= models.ForeignKey(Estudiante)
    puntuacion= models.IntegerField()
    fecha=models.DateTimeField(auto_now=True,null=True,blank=True)

    def __unicode__(self):
        return str(self.puntuacion)

class Docente(Persona):

    def __unicode__(self):
         return  self.primer_nombre + " "+self.primer_apellido+" "+self.segundo_apellido