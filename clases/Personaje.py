class Personaje:
    #CONSTRUCTOR
    def __init__(self, name, age):
        #ATRIBUTOS(1 guionbajo despues del punto es para protejer los datos PROTECTED
        # 2 guiones bajos son PRIVATE)
        self.__nombre=name
        self.__edad=age

    
    #metodos GET (obtener el valor de un atrivuto)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad


    #metodos SET (Llevar un valor a un atributo) En los metodos SET se hace la validacion de los datos
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre=nombre

    
    @edad.setter
    def edad(self, edad):
        if(edad<0):
            print("NO ES VALIDO")
        else:
            self.__edad=edad


