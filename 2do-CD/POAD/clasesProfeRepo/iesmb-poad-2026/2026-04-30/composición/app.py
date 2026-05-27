from datetime import date
from perfil import Perfil
from usuario import Usuario

def main():
    u: Usuario = Usuario("xd", "1234", Perfil("el peluca sapeee", date(2000,11,30)))
    print(u)
    pwd: str = input("¿Contraseña? ")
    print("¡Correcto!" if u.autenticar(pwd) else "Nope...")

if __name__ == "__main__":
    main()