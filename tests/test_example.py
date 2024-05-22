"""Example test case for the project. It is good practice to have test functions within a tests directory."""
import pytest
import template3 as tp
import math

# All functions starting with 'test_' are considered as test cases.
def test_simple_case():
    assert (1 + 2) == 3, "Addition Works"


def test_global_data_dir():
    a = tp.utils.global_data_dir()
    assert isinstance(a, str)

@pytest.mark.parametrize("test_input, expected", [(25,5), (81,9)])
def test_square_root(test_input, expected):
    assert math.sqrt(test_input) == expected
