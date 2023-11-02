from src.ejercicio9 import *
import pytest

@pytest.mark.parametrize(
    "frase, vocal, expected", 
    [
        ("manzana", "a", 3),
        ("platano", "a", 2),
        ("ojo", "o", 2),
        ("esternocleidomastuideo", "e", 4)
    ])
def test_contarPalabras(frase, vocal, expected):
        assert contarPalabras(frase, vocal) == expected