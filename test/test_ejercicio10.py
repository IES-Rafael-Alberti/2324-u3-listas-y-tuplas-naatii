from src.ejercicio10 import obtenerMayor, obtenerMenor
import pytest
@pytest.mark.parametrize(
    "input_list, expected_output", 
    [
        ([1, 2, 3, 4, 5], 5),
        ([10, 20, 30, 40, 50], 50),
        ([-1, -2, -3, -4, -5], -1),
        ([-10, -20, -30, -40, -50], -10)
    ])
def test_obtenerMayor(input_list, expected_output):
        assert obtenerMayor(input_list) == expected_output
@pytest.mark.parametrize(
    "lista, expected", [
        ([50, 75, 46, 22, 80, 65, 8], 8),
        ([1, 2, 3, 4, 5], 1),
        ([10, 20, 30, 40, 50], 10),
    ])
def test_returns_minimum_value(lista, expected):
        assert obtenerMenor(lista) == expected