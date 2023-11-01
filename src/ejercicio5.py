def ordenarInverso(numeros:list)->list:
    """Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

    Args:
        numeros (list): Lista con los números del 1 al 10.

    Returns:
        list: La lista con los números ordenados en orden inverso.
    """
    numeros.sort(reverse=True)
    return numeros

if __name__=="__main__":
    numeros = list(range(1,11))
    print(ordenarInverso(numeros))