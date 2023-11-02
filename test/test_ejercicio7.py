from src.ejercicio7 import *
   
def test_eliminarLetras():
        abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        expected_result = ['b', 'c', 'e', 'f', 'h', 'i', 'k', 'l', 'n', 'ñ', 'p', 'q', 's', 't', 'v', 'w', 'y']
        assert eliminarletras(abecedario) == expected_result