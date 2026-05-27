from dataclasses import dataclass

@dataclass
class Persona:
    nombre: str
    edad: int
    peso: float
    def presentarse(self):
        print(f"Hola, soy {self.nombre}.")