from dataclasses import dataclass
from perfil import Perfil

@dataclass
class Usuario:
    nick: str
    _pwd: str
    perfil: Perfil
    def autenticar(self, pwd: str) -> bool:
        return self._pwd == pwd
    def __str__(self) -> str:
        return f"""Usuario: {self.nick}
{self.perfil}"""
