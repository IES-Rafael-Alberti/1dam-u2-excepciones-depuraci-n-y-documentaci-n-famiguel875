import pytest

from src.ejercicio_2_3_2 import obtener_impares_hasta_n

def test_obtener_impares_hasta_n():
    assert obtener_impares_hasta_n(5) == ['1', '3', '5']
    assert obtener_impares_hasta_n(0) == []
    assert obtener_impares_hasta_n(1) == ['1']
    with pytest.raises(ValueError):
        obtener_impares_hasta_n(-5)
    with pytest.raises(ValueError):
        obtener_impares_hasta_n("abc")