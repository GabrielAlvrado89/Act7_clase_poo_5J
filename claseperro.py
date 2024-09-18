print("Programación POO")
# definicion de clases
class Perro:
    # funciones dentro de la clase 
    def morder(self):
        print("El perro me mordió")
    def Datos_perro(self,nombre,edad):
        print(f" Nombre: {nombre} edad : {edad}")
# zona de creacion de objeto
pitbull=Perro()


# zona de uso de objetos
pitbull.Datos_perro("Canelita",4)
pitbull.morder()