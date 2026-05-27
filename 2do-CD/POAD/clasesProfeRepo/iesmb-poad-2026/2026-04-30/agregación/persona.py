from dataclasses import dataclass, field
from vehiculo import Vehiculo

@dataclass
class Persona:
    nombre: str
    edad: int
    peso: float
    vehiculos: list[Vehiculo] = field(default_factory=list[Vehiculo], init=False)
    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")
        if len(self.vehiculos):
            print("Mis vehículos son: {}.".format(
                ", ".join([v.patente for v in self.vehiculos])))
        else:
            print("No tengo vehículos.")