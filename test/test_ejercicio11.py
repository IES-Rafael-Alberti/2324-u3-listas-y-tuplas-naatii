from src.ejercicio11 import productoEscalar
def test_correct_product():
        lista1 = [1, 2, 3]
        lista2 = [-1, 0, 2]
        assert productoEscalar(lista1, lista2) == 5