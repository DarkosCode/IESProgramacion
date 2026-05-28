from dataclasses import dataclass
#* Funcionalidad que introdujo Python para evitar codigo repetitivo;
#* se usa para crear clases que almacenan informacion sin escribir todo el constructor y demas

@dataclass
class Vehiculo:
    patente: str
