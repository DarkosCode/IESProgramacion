from persona import Persona
from vehiculo import Vehiculo

def main():
    p: Persona = Persona("fulano", 22, 60)
    v: Vehiculo = Vehiculo("ab 123 cd")
    p.presentarse()
    print(v)
    v.propietario = p
    print(v)

if __name__ == "__main__":
    main()