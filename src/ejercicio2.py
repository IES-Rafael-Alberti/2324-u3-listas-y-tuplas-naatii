def asignaturas()->list:
    """Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.

    Returns:
        list: Devuelve una lista con 5 asignaturas.
    """
    return "matemáticas", "física", "química", "historia", "lengua"

    # > En el ejercicio indica que debe ser una lista pero al ser valores que no van a ser modificados he decidido usar una tupla para este cometido

if __name__=="__main__":
    for asignatura in asignaturas():
        print(f"yo estudio {asignatura}")