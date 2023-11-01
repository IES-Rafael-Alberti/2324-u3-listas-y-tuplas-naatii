from src.ejercicio4 import *
import pytest

@pytest.mark.parametrize("numeros, expected", [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([9, 5, 7, 6], [5, 6, 7, 9]),
        ([100, 200, 50, 75], [50, 75, 100, 200])
    ])
def test_sort_integers(numeros, expected):
        # Act
        result = ordenarNumeros(numeros)

        # Assert
        assert result == expected
    # Returns True when given a valid positive integer as a string
@pytest.mark.parametrize(
    "input, expected", 
    [
        ("123", True),
        ("456", True), 
        ("789", True),
        ("a", False),
        ("", False),
    ])
def test_valid_positive_integer(input, expected):
    assert comprobarNumero(input) == expected