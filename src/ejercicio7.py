def eliminarletras(abecedario:list)->list:
    """
    Escribir un programa que almacene en una lista los caracteres de un abecedario.
    Args:
        abecedario (list): Lista con los caracteres de un abecedario.
    Returns:
        list: Lista con los caracteres de un abecedario.
    """
    abecedarioDeMultiplosDeTres = [] 

    for i in range(0, len(abecedario)-1, 3):
        abecedarioDeMultiplosDeTres.append(abecedario[i])
    return abecedarioDeMultiplosDeTres

if __name__ == "__main__":
    abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print(len(abecedario))
    print(eliminarletras(abecedario))