from src.ejercicio13 import *
import pytest

@pytest.mark.parametrize("lista, expected", [
        ([1, 2, 3, 4, 5], 3.0),
        ([10, 20, 30, 40, 50], 30.0),
        ([2, 4, 6, 8, 10], 6.0)
    ])
def test_calcularMedia(lista, expected):
        assert calcularMedia(lista) == expected
@pytest.mark.parametrize("lista, expected", [
        ([1, 2, 3, 4, 5], 1.4142135623730951),
        ([1.5, 2.5, 3.5, 4.5, 5.5], 1.4142135623730951),
        ([10], 0.0),
        ([-1, -2, -3, -4, -5], 1.4142135623730951)
    ])
def test_calcularDesviacionTipica(lista, expected):
        result = calcularDesviacionTipica(lista)
        assert result == expected
def test_calcularMediaConListaVacia():
    with pytest.raises(ValueError):
        calcularMedia([])
def test_calcularDesviacionTipicaConListaVacia():
    with pytest.raises(ValueError):
        calcularDesviacionTipica([])
