import unittest
from batalla_naval import JuegoBatallaNaval, Barco

class TestJuegoBatallaNaval(unittest.TestCase):
    def setUp(self):
        self.juego = JuegoBatallaNaval()

    def test_inicializacion_tablero(self):
        """Verifica que el tablero sea 10x10"""
        self.assertEqual(len(self.juego.tablero), 10)
        self.assertEqual(len(self.juego.tablero[0]), 10)

    def test_cantidad_barcos(self):
        """Verifica que se hayan creado 9 barcos en total"""
        # 4 de tamaño 1 + 3 de tamaño 2 + 2 de tamaño 3 = 9 barcos
        self.assertEqual(len(self.juego.flota), 9)

    def test_barcos_no_superpuestos(self):
        """Verifica que el número de celdas ocupadas coincida con la suma de tamaños"""
        celdas_ocupadas = 0
        for fila in self.juego.tablero:
            for celda in fila:
                if celda is not None:
                    celdas_ocupadas += 1
        
        # 4*1 + 3*2 + 2*3 = 4 + 6 + 6 = 16 celdas ocupadas
        self.assertEqual(celdas_ocupadas, 16)

    def test_disparo_agua(self):
        """Verifica disparo al agua"""
        # Buscamos una celda vacía
        for f in range(10):
            for c in range(10):
                if self.juego.tablero[f][c] is None:
                    estado, barco = self.juego.disparar(f, c)
                    self.assertEqual(estado, "AGUA")
                    self.assertIsNone(barco)
                    return

    def test_hundir_barco_tamano_1(self):
        """Verifica hundir un barco de tamaño 1"""
        # Encontrar un barco de tamaño 1
        for barco in self.juego.flota:
            if barco.tamano == 1:
                # Buscar sus coordenadas
                for f in range(10):
                    for c in range(10):
                        if self.juego.tablero[f][c] == barco:
                            estado, b_hundido = self.juego.disparar(f, c)
                            self.assertEqual(estado, "HUNDIDO")
                            self.assertEqual(b_hundido, barco)
                            self.assertTrue(barco.esta_hundido())
                            return

if __name__ == '__main__':
    unittest.main()
