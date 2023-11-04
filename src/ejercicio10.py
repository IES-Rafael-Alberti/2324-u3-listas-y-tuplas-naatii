def obtenerMayor(lista:list)->int:
    """Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.

    Args:
        lista (list): Lista con los precios.

    Returns:
        int: Numero mayor de los precios.
    """
    return max(lista)
def obtenerMenor(lista:list)->int:
    """Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.

    Args:
        lista (list): Lista con los precios.

    Returns:
        int: Numero menor de los precios.
    """
    return min(lista)

if __name__=="__main__":
    precios = [50, 75, 46, 22, 80, 65, 8]
    print(f"Este es el precio más alto -> {obtenerMayor(precios)}")
    print(f"Este es el menor de los precios -> {obtenerMenor(precios)}")