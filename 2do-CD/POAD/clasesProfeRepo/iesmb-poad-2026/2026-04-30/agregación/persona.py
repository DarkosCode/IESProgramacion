from dataclasses import dataclass, field
from vehiculo import Vehiculo

@dataclass
class Persona:
#* @dataclass: Las clases de datos de Python necesitan que les indiques
#* el tipo de dato mediante estas anotaciones (llamadas type hints)
    nombre: str
    edad: int
    peso: float
    vehiculos: list[Vehiculo] = field(default_factory=list[Vehiculo], init=False)
    #* init=False hace que el constructor no me pida de forma obligatoria que a Persona le pase si o si
    #* una lista de vehiculos
    #! El default_factory = list[] hace que cada vez que se crea una nueva persona, se le fabrica una lista
    #! en blanco desde cero. Si no se hiciera asi se apuntaria siempre al mismo espacio de memoria.
    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        if len(self.vehiculos):
            print("Mis vehículos son: {}.".format(
                ", ".join([v.patente for v in self.vehiculos])))
        else:
            print("No tengo vehículos.")