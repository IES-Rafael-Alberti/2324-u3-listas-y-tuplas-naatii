def calcularMedia(lista:list)->float:
    """Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media.

    Args:
        lista (list): Lista de números separados por comas.

    Returns:
        float: Resultado de la media.
    """

    if len(lista) == 0:
        raise ValueError("No se puede calcular la media de una lista vacía")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    return sum(lista) / len(lista)
def calcularDesviacionTipica(lista:list)->float:
    """Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla desviación típica.

    Args:
        lista (list): Lista de números separados por comas.

    Returns:
        float: Resultado de la desviación típica.
    """
    if len(lista) == 0:
        raise ValueError("No se puede calcular la media de una lista vacía")
    for i in range(len(lista)):
        lista[i] = int(lista[i])
    media = sum(lista) / len(lista)
    desviacion_tipica = 0
    for i in lista:
        desviacion_tipica += ((i - media) ** 2) / len(lista)
    return desviacion_tipica ** 0.5

if __name__=="__main__":
    try:
        numeros = input("Ingrese números separados por comas: ").split(",")
        media = calcularMedia(numeros)
        desviacionTipica = calcularDesviacionTipica(numeros)
        print(f"La media es: {media}")
        print(f"La desviación típica es: {desviacionTipica}")
    except ValueError:
        print(ValueError())