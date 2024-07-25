from flask import Flask, request, redirect, render_template, url_for
import json

app = Flask(__name__)

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
    
    def guardar(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.__dict__, f, default=lambda o: o.__dict__, indent=4)
            
class Serpiente:
    def __init__(self, nombre, longitud, especie):
        self.nombre = nombre
        self.longitud = longitud
        self.especie = especie

    def deslizarse(self):
        print(f"la serpiente {self.nombre} de la especie {self.especie} se está deslizando")

@app.route('/')
def index():
    return render_template('terrario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre_terrario = request.form.get('nombre_terrario')
    ancho = request.form.get('ancho')
    largo = request.form.get('largo')
    nombre_serpiente = request.form.get('nombre_serpiente')
    longitud = request.form.get('longitud')
    especie = request.form.get('especie')

    terrario = Terrario(nombre_terrario, ancho, largo)
    serpiente = Serpiente(nombre_serpiente, longitud, especie)
    terrario.agregar_habitante(serpiente)
    terrario.guardar('terrario.json')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

#crear instancias (terrario y serpientes)
new_terrario = Terrario("Terrario Verano", 5, 5, [])
serpiente1 = Serpiente("Anaconda", 2.5, "Eunectes murinus")
serpiente2 = Serpiente("Piton", 3, "Pythonidae")

#añadir las serpientes al terrario
new_terrario.agregar_habitante(serpiente1)
new_terrario.agregar_habitante(serpiente2)

#calcular el area del terrario y mostrar resultado:
area_terrario = new_terrario.area()
print(f'El área del terrario es {area_terrario} cm.')

#mostrar las serpientes:
print(f'los habitantes del terrario son:')
for serpiente in new_terrario.habitantes:       
    print(f'{serpiente.nombre}')
serpiente1.deslizarse()
serpiente2.deslizarse()