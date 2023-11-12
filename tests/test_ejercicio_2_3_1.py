import pytest
from src.ejercicio_2_3_1 import anios_cumplidos

def test_anios_cumplidos():
    assert anios_cumplidos(5) == [1, 2, 3, 4, 5]
    assert anios_cumplidos(0) == []
    assert anios_cumplidos(1) == [1]
    assert anios_cumplidos(10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_anios_cumplidos_con_valor_invalido():
    with pytest.raises(ValueError):
        anios_cumplidos("abc")

def test_anios_cumplidos_con_valor_negativo():
    with pytest.raises(ValueError):
        anios_cumplidos(-5)