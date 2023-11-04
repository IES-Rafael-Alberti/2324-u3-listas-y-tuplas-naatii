def productoMatriz(lista1:list, lista2:list)->float:
    """Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

    Args:
        lista1 (list): matriz A.
        lista2 (list): matriz B.

    Returns:
        float: resultado del producto de la matriz.
    """
    return lista1[0] * lista2[0] + lista1[1] * lista2[1] + lista1[2] * lista2[2] + lista1[3] * lista2[3] + lista1[4] * lista2[4] + lista1[5] * lista2[5] + lista1[6] * lista2[6] + lista1[7] * lista2[7] + lista1[8] * lista2[8]

if __name__=="__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista2 = [-1, 0, 1, 2, 3, 4, 5, 6, 7]
    print(f"Este es el producto de la matriz -> {productoMatriz(lista1, lista2)}")