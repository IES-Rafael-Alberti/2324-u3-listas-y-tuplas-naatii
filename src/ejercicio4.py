def ordenarNumeros(numeros:list)->list:
    numeros.sort()
    return numeros

# TODO: intentar implementar esto
# def comprobarLista(numeros:list, numero:int):
#     if numero not in numeros:
#         return True
#     else:
#         return False

# ? Qué debería ir en una función y que no?

def comprobarNumero(numero:str)->bool:
    if numero.strip().isdigit():
        return True
    else:
        return False

if __name__=="__main__":
    numeros = []
    TAMAÑOLISTA = 6
    while len(numeros)<TAMAÑOLISTA:
        numero = input("Introduce un número de la secuencia ganadora: ")
        if comprobarNumero(numero):
            numeros.append(int(numero))
        else:
            print("ERROR: Introduce un número de la secuencia ganadora")
    print(ordenarNumeros(numeros))