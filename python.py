class Terrario:
    def __init__(self, nombre, ancho, largo, habitantes):
        self.nombre = nombre
        self.ancho = ancho
        self.largo = largo
        self.habitantes = []
    def agregar_habitante(self, serpiente):
        self.habitantes.append(serpiente)
    def area(self):
        return self.ancho * self.largo
    
class Serpiente:
    def __init__(self, nombre, longitud, especie):
        self.nombre = nombre
        self.longitud = longitud
        self.especie = especie
    def deslizarse(self):
        print(f"la serpiente {self.nombre} de la especie {self.especie} se está deslizando")

#crear instancias (terrario y serpientes)
new_terrario = Terrario("Terrario Verano", 5, 5, [])
serpiente1 = Serpiente("Anaconda", 2.5, "Eunectes murinus")
serpiente2 = Serpiente("Piton", 3, "Pythonidae")

#añadir las serpientes al terrario
new_terrario.agregar_habitante(serpiente1)
new_terrario.agregar_habitante(serpiente2)

#calcular el area del terrario y mostrar resultado:
area_terrario = new_terrario.area()

#print(f"el area del terrario es {area_terrario} metros cuadrados")
#mostrar las serpientes del terrario:
#print(f"los habitantes del terrario {new_terrario.nombre} son:")
#for serpiente in new_terrario.habitantes:
    #print(f"{serpiente.nombre} ({serpiente.especie}, {serpiente.longitud} metros)")

# Hacer que las serpientes se deslicen
#serpiente1.deslizarse()
#serpiente2.deslizarse()

class Zoologico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.terrarios = []
    def agregar_terrario(self, terrario):
        self.terrarios.append(terrario)
    def mostrar_serpientes(self):
        print(f"Todas las serpientes en el zoologico {self.nombre}:")
        for terrario in self.terrarios:
            print(f"Terrario: {terrario.nombre} (Área: {terrario.area()} metros cuadrados)")
            for serpiente in terrario.habitantes:
                print (f"{serpiente.nombre} ({serpiente.especie}, {serpiente.longitud} metros)")
zoo = Zoologico("Zoo central")
zoo.agregar_terrario(new_terrario)
zoo.mostrar_serpientes()
serpiente1.deslizarse()
serpiente2.deslizarse()