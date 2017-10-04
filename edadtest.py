# coding=utf-8

import unittest
from edad import Edad
import io
from contextlib import redirect_stdout


class EdadTest(unittest.TestCase):
    # Test fixtures

    def setUp(self):
        self.edad = Edad()
        self.out = io.StringIO()

    def tearDown(self):
        pass

    # Prueba del valor de inicio

    def test_datos_invalidos(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad('a')
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida,
                         'debes insertar un número')

    def test_recien_nacido(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(0)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres un recién nacido')

    def test_inexistente(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(-1)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'no existes')

    def test_nino(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(12)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres niño')

    def test_adolescente(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(17)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres adolescente')

    def test_adulto(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(64)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres adulto')

    def test_adulto_mayor(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(119)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres adulto mayor')

    def test_mumm_ra_1(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(120)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres Mumm-Ra')

    def test_mumm_ra_2(self):
        with redirect_stdout(self.out):
            self.edad.evaluar_edad(121)
        salida = self.out.getvalue().replace('\n', '')
        self.assertEqual(salida, 'eres Mumm-Ra')


# Ejecuta las pruebas implementadas
if __name__ == '__main__':  # pragma: no cover
    unittest.main()
