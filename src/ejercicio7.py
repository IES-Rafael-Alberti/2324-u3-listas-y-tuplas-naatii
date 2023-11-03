def eliminarletras(abecedario:list)->list:
    """
    Escribir un programa que almacene en una lista los caracteres de un abecedario.
    Args:
        abecedario (list): Lista con los caracteres de un abecedario.
    Returns:
        list: Lista con los caracteres de un abecedario.
    """
    abecedario[::3] 
    return abecedario
    

if __name__ == "__main__":
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(eliminarletras(abecedario))