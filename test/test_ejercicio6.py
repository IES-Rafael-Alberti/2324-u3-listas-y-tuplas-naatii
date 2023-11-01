from src.ejercicio6 import *
import pytest
    # The function receives a tuple with the names of the subjects and a list with the grades of each subject, and returns a string with the name of the subjects that the student failed and their respective grades.
@pytest.mark.parametrize(
    "asignaturas, notas, expected_output", 
    [
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["4", "6", "a", "7", "5"], "En Matemáticas has sacado 4\nEn Química has sacado 0\n"),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["6", "7", "8", "9", "10"], ""),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), [" ", "2", "2", "2", "2"], "En Matemáticas has sacado 0\nEn Física has sacado 2\nEn Química has sacado 2\nEn Historia has sacado 2\nEn Lengua has sacado 2\n"),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["5", "5", "5", "5", "5"], ""),
        (("Matemáticas", "Física", "Química", "Historia", "Lengua"), ["6", "4", "7", "-3", "5"], "En Física has sacado 4\nEn Historia has sacado 0\n"),
    ])
def test_failed_subjects_and_grades(asignaturas, notas, expected_output):
        # Act
        result = mensajeNotasAsignaturas(asignaturas, notas)

        # Assert
        assert result == expected_output