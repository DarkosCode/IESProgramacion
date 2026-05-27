from dataclasses import dataclass, field
from persona import Persona

@dataclass
class Vehiculo:
    patente: str
    propietario: Persona | None = field(default=None, init=False)
    def __str__(self):
        if self.propietario:
            return f"El vehículo {self.patente} tiene al propietario {self.propietario}."
        else:
            return f"El vehículo {self.patente} no tiene propietario."