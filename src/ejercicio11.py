def productoEscalar(lista1:list, lista2:list)->float:
    """Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

    Args:
        lista1 (list): La primera lista de vectores.
        lista2 (list): La segunda lista de vectores.

    Returns:
        float: El resultado del producto escalar.
    """
    return (lista1[0] * lista2[0]) + (lista1[1] * lista2[1]) + (lista1[2] * lista2[2])

if __name__=="__main__":
    lista1 = [1, 2, 3]
    lista2 = [-1, 0, 2]
    print(f"Este es el producto escalar -> {productoEscalar(lista1, lista2)}")