
def mensajeNotasAsignaturas(asignaturas:tuple, notas:list)->str:
    """
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

    Args:
        asignaturas (tuple): Tupla con las asignaturas
        notas (list): Lista de notas por cada asignatura

    Returns:
        str: Mensaje que se va imprimir con la nota de cada asignatura.
    """
    mensaje = ""
    for asignatura, nota in zip(asignaturas, notas): # ! zip sirve para empaquetar
        if nota.strip().isdigit() :
            if int(nota)>=5:
                asignatura = ""
            else:
                mensaje += (f"En {asignatura} has sacado {nota}\n")
        else:
            mensaje += (f"En {asignatura} has sacado {0}\n")
    return mensaje

# TODO: Refactorizar el código.

if __name__=="__main__":
    asignaturas = ["matemáticas", "física", "química", "historia", "lengua"]

    # > En el ejercicio indica que debe ser una lista pero al ser valores que no van a ser modificados he decidido usar una tupla para este cometido
    notas = []
    for asignatura in asignaturas:
        notas.append(input(f"Introduce la nota para la asignatura {asignatura}: "))
        
    print(f"\n{'-'*100}\n")
    print(mensajeNotasAsignaturas(asignaturas, notas))