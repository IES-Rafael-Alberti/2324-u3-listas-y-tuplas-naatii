from src.ejercicio7 import *
   
def test_eliminarLetras():
        abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        expected_result = ['a', 'd', 'g', 'j', 'm', 'o', 'r', 'u', 'x']
        assert eliminarletras(abecedario) == expected_result