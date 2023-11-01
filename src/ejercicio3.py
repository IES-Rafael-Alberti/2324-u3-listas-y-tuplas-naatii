def asignaturas()->list:
    """Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

    Returns:
        list: Devuelve una lista con 5 asignaturas.
    """
    return "matemáticas", "física", "química", "historia", "lengua"

    # > En el ejercicio indica que debe ser una lista pero al ser valores que no van a ser modificados he decidido usar una tupla para este cometido

def mensajeNotasAsignaturas(asignaturas:list, notas:list)->str:
    mensaje = ""
    for asignatura, nota in zip(asignaturas, notas): # ! zip sirve para empaquetar
        if nota == "" or nota.isspace():
            nota = 0
        mensaje += (f"En {asignatura} has sacado {nota}\n")
    return mensaje

# TODO: Refactorizar el código.

if __name__=="__main__":
    notas = []
    for asignatura in asignaturas():
        notas.append(input(f"Introduce la nota para la asignatura {asignatura}: "))
    print(f"\n{'-'*100}\n")
    print(mensajeNotasAsignaturas())