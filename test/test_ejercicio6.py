from src.ejercicio6 import *
import pytest
@pytest.mark.parametrize(
    "asignaturas, notas, expected_output", 
    [
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["4", "6", "a", "7", "5"], "En Matemáticas has sacado 4\nEn Química has sacado 0\n"),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["6", "7", "8", "9", "10"], ""),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), [" ", "2", "2", "2", "2"], "En Matemáticas has sacado 0\nEn Física has sacado 2\nEn Química has sacado 2\nEn Historia has sacado 2\nEn Lengua has sacado 2\n"),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["5", "5", "5", "5", "5"], ""),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["6", "4", "7", "-3", "5"], "En Física has sacado 4\nEn Historia has sacado 0\n"),
    ])
def test_mensajeNotasAsignaturas(asignaturas, notas, expected_output):
        assert mensajeNotasAsignaturas(asignaturas, notas) == expected_output
       