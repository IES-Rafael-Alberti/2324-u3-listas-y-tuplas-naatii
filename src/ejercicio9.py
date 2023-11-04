def contarLetras(word:str)->int:
    """Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

    Args:
        palabra (str): La palabra ingresada por el usuario.

    Returns:
        int: El número de veces que contiene cada vocal en la palabra ingresada por el usuario.
    """
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    return times

if __name__=="__main__":
    word = input("Introduce una palabra: ")
    vocals = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocals: 
        times = contarLetras(word)
        print("La vocal " + vocal + " aparece " + str(times) + " veces")