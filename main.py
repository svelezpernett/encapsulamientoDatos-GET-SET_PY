#IMPORTAR LA CLASE
from clases.Personaje import Personaje

#INSTANCIO LA CLASE POR MEDIO DE LA CREACION DE UN OBJETO
personaje=Personaje("Juan", 800)

#Accediendo a los metodos SETTER (SET)
personaje.nombre="KATALINA"
personaje.edad=30

#Accediendo a los metodos GET
print(personaje.nombre)
print(personaje.edad)
