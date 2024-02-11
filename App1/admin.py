from django.contrib import admin
#Importando los modelos a admin para verlos en el administrador de BD al iniciar sesion
from .models import AutorDB,FraseBD,ProfesionDB

#Registrando otro modelo
@admin.register(ProfesionDB)
class ProfeionAdmin(admin.ModelAdmin):
    fields = ['nombre']
    list_display = ['nombre']


# Creando la clase para unir tanto la creacion de author y la frase
class FraseInLine(admin.TabularInline):
    model = FraseBD
    extra = 1

# Creacion de la clase y dando nombre para saber que es para mostrar en admin
class AutorAdmin(admin.ModelAdmin):
    fields = ['nombre', 'fecha_nacimiento','fecha_fallecimiento','profesion','nacionalidad']
    list_display = ['nombre', 'fecha_nacimiento']

    #Insertando el inline
    inlines = [FraseInLine]

    #Creando acciones
    def actualizar_o(self, request, queryset):
        for obj in queryset:
            if "O" in obj.nombre:
                nombre_modificado = obj.nombre.replace("O", "o")
                obj.nombre = nombre_modificado
                obj.save()

        self.message_user(request, "Exitosamente")

    actualizar_o.short_description = "Actualizar letras O"

    #Registrar la accion en admin
    actions = ['actualizar_o']

#Registrando las clase en admin
admin.site.register(AutorDB,AutorAdmin)

#Se crea la clase y se registra con un decorador
@admin.register(FraseBD)
class FraseAdmin(admin.ModelAdmin):
    fields = ['cita','autor_fk']
    list_display = ['cita','autor_fk']



