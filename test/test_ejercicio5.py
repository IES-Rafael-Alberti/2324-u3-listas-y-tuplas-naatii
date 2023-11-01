from src.ejercicio5 import ordenarInverso
import pytest
    # The function correctly sorts a list of integers in descending order.
@pytest.mark.parametrize("input_list, expected_output", [
        ([5, 2, 8, 1, 9], [9, 8, 5, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [9, 8, 7, 6, 5, 4, 3, 2, 1])
    ])
def test_sort_descending_order(input_list, expected_output):
        # Act
        result = ordenarInverso(input_list)

        # Assert
        assert result == expected_output