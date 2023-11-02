def contarPalabras(frase:str, vocal:str)->int:
    """Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

    Args:
        palabra (str): La palabra ingresada por el usuario.

    Returns:
        int: El número de veces que contiene cada vocal en la palabra ingresada por el usuario.
    """
    contador = 0
    for letra in frase.lower():
        if letra == vocal.lower():
            contador += 1
    return contador

if __name__=="__main__":
    frase = input("Ingrese una palabra: ")
    vocal = input("Ingrese una vocal: ")
    print(contarPalabras(frase, vocal))