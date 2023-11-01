from src.ejercicio3 import *
import pytest

@pytest.mark.parametrize(
    "asignaturas, notas, expected",
    [
        (("matemáticas", "física", "química", "historia", "lengua"), ["5", "9", "  ", "a", ""], "En matemáticas has sacado 5\nEn física has sacado 9\nEn química has sacado 0\nEn historia has sacado 0\nEn lengua has sacado 0\n")
    ]
)
def test_returns_string_with_grades_and_message(asignaturas, notas, expected):
    assert mensajeNotasAsignaturas(asignaturas, notas) == expected