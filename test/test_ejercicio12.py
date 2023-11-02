from src.ejercicio12 import productoMatriz
def test_product_of_matrices():
        # Arrange
        lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        lista2 = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    
        # Act
        result = productoMatriz(lista1, lista2)
    
        # Assert
        assert result == 195