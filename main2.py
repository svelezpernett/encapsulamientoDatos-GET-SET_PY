from ast import Str
from clases.Escuderias import Escuderias
from operator import attrgetter

arregloEscuderias=[]
arregloFerrari=[]
arregloMercedez=[]
arregloRenault=[]

def ingresarEscuderia():
    
    e=input("Presione cualquier tecla, y * al terminar")
    while(e!="*"):

        escuderia=Escuderias("Ferrari", "Motor Ferrari", "Sainz", 0)

        name=input("ingrese el nombre de la escuderia ")
        engine=input("ingrese el motor ")
        pilot=input("ingrese el piloto ")
        cost=int(input("ingrese el costo anual "))


        escuderia.nombre=name
        escuderia.motor=engine
        escuderia.piloto=pilot
        escuderia.costo=cost
        arregloEscuderias.append(escuderia)

        if(escuderia.motor=="ferrari"):
            arregloFerrari.append(escuderia)
        else:
            if(escuderia.motor=="mercedez"):
                arregloMercedez.append(escuderia)
            else:
                if(escuderia.motor=="renault"):
                    arregloRenault.append(escuderia)

        print(arregloEscuderias)
        
        e=input("Ingrese * para finalizar o cualquier tecla para añadir otra escuderia")

ingresarEscuderia()

for objeto in arregloEscuderias:
    print("ESCUDERIA: " + objeto.nombre)
    print("MOTOR: " + objeto.motor)
    print("PILOTO: " + objeto.piloto)
    print("COSTO ANUAL: ", objeto.costo, sep="")

maxCost=(max(arregloEscuderias, key=attrgetter('costo')))
print(f"COSTO MAXIMO ANUAL ES DE LA ESCUDERIA {maxCost.nombre} DE ", maxCost.costo, sep="")

print("Numero de motores Ferrari: "+str(len(arregloFerrari)))
print("Numero de motores Mercedez: "+str(len(arregloMercedez)))
print("Numero de motores Renault: "+str(len(arregloRenault)))








