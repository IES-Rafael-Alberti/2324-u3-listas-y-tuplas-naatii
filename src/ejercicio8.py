def palindromo(palabra:str)->bool:
    """Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
    Args:
        palabra (str): La palabra que se desea verificar si es un palíndromo.
    Returns:
        buleando si la palabra es un palíndromo.
    """
    if palabra.lower() == palabra[::-1].lower():
        return True
    else:
        return False

if __name__=="__main__":
    palabra = input("Ingrese una palabra: ")
    if palindromo(palabra):
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")