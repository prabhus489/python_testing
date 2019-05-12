import pytest
from python_codes.mathlib import calc_total, calc_multiply

def test_calc_total():
    total=calc_total(4,5)
    assert total == 9

def test_calc_multiply():
    result=calc_multiply(10,3)
    assert result == 30

