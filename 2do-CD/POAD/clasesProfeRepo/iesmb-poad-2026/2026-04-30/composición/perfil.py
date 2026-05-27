from dataclasses import dataclass
from datetime import date

@dataclass
class Perfil:
    bio: str
    nacimiento: date
    """Este atributo también es una composición, pero al ser date una clase nativa, 
    no debe ser graficada en el diagrama de clases.
    """
    def __str__(self) -> str:
        return f"""Nacimiento: {self.nacimiento.strftime("%d/%m/%Y")}
Biografía: {self.bio}"""
