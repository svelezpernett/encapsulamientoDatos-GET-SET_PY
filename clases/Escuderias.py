from pickle import TRUE


class Escuderias:
    def __init__(self, name, engine, pilot, cost):
        self.__nombre=name
        self.__motor=engine
        self.__piloto=pilot
        self.__costo=cost


    @property
    def nombre(self):
        return self.__nombre

    @property
    def motor(self):
        return self.__motor

    @property
    def piloto(self):
        return self.__piloto

    @property
    def costo(self):
        return self.__costo
    


        

    @nombre.setter
    def nombre(self, nombre):
        if (nombre.isdigit() is False and len(nombre)>0):
            self.__nombre=nombre 
        else:
            print("NOMBRE NO VALIDO")

    
    @motor.setter
    def motor(self, motor):
        if (motor.isdigit() is False and len(motor)>0):
            self.__motor=motor
        else:
            print("MOTOR NO VALIDO")

    @piloto.setter
    def piloto(self, piloto):
        if (piloto.isdigit() is False and len(piloto)>0):
            self.__piloto=piloto
        else:
            print("PILOTO NO VALIDO")

    @costo.setter
    def costo(self, costo):
        if(costo<=0):
            print("COSTO NO VALIDO")
        else:
            self.__costo=costo
