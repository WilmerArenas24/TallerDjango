from django.db import models

#aqui creamos nuestros modelos de BD

#Creamos una normalizacion en la profesion
class ProfesionDB(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre',null=False)

    def __str__(self):
        return self.nombre

class AutorDB(models.Model):
    nombre = models.CharField(max_length=200, verbose_name='Nombre',null=False)
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento',null=False, blank=False)
    fecha_fallecimiento = models.DateField(verbose_name='Fecha Fallecimiento',null=True, blank=True)
    #Le pasamos la profesion de la clase Profesion creada para normalizacion
    profesion = models.ManyToManyField(ProfesionDB, verbose_name='Profesion')
    nacionalidad = models.CharField(verbose_name='Nacionalidad', max_length=200)

    # Creando la clase para modificar la clase tanto en administrador como en la BD
    class Meta:
        db_table = "Autores"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    # Funcion para poner mas presentable nuestros registros en las peticiones
    def __str__(self):
        return self.nombre



class FraseBD(models.Model):
    cita = models.TextField(verbose_name='Cita', max_length=500)
    autor_fk = models.ForeignKey(AutorDB, on_delete=models.CASCADE)

    # Creando la clase para modificar la clase tanto en administrador como en la BD
    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    # Funcion para poner mas presentable nuestros registros en las peticiones
    def __str__(self):
        return self.cita



