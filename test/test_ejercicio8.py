from src.ejercicio8 import *
import pytest

@pytest.mark.parametrize(
    "palabra,expected",
    [
        ("palabra", False),
        ("", True),
        ("Ana", True),
        ("oso", True)
    ]
)

def test_palindromo(palabra, expected):
    assert palindromo(palabra) == expected