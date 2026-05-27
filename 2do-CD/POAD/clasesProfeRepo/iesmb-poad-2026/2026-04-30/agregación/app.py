from persona import Persona
from vehiculo import Vehiculo

def main():
    p: Persona = Persona("fulano", 22, 60)
    p.presentarse()
    p.agregar_vehiculo(Vehiculo("ab 123 cd"))
    p.presentarse()
    p.agregar_vehiculo(Vehiculo("ef 456 gh"))
    p.presentarse()

if __name__ == "__main__":
    main()