def ordenarInverso(numeros:list)->list:
    numeros.sort(reverse=True)
    return numeros

if __name__=="__main__":
    numeros = list(range(1,11))
    print(ordenarInverso(numeros))