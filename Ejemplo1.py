#camel case: son buenas practicas
'''
class Cliente:    #se creea una clase publica 
    documento  = ""
    nombre = "Derly Maria"
    correo = ""
    edad = 0
       
#instanciar: crear un objeto de la clase 

objeto = Cliente()

print (objeto.nombre)
'''
#solo se puede crear un constructor en python 
#los metodos siempre tienen que tener la palabra (SELF)se deja mas espacio de memoria RAN y define que es un metodo en la misma memiria RAM, ademas de siempre comenzar con minuscula para diferenciarse de los constructores
class Cliente: 
    def __init__(self, doc,nom,cor,eda):#asi se crea un constructor de la clase y tiene variable que van a almacenar los atributos
        self.__documento = doc
        self.__nombre = nom
        self.__correo = cor
        self.__edad = eda
        

    #get: para llamar a la informacion que esta guardada en las variables, 
    #def: declarar metodos
    def get_Documento(self):
        return self.__documento
    def set_Documento(self, documento):
        self.__documento = documento

    def get_Nombre(self):
        return self.__nombre
    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def get_Correo(self):
        return self.__correo
    def set_Correo(self, correo):
        self.__correo = correo

    def get_Edad(self):
        return self.__edad
    def set_Edad(self, edad):
        self.__edad = edad
