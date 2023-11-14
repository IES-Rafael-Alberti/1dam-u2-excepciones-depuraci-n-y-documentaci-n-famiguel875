import pytest

from src.ejercicio_2_3_3 import obtener_cuenta_atras

def test_obtener_cuenta_atras():
    assert obtener_cuenta_atras(5) == '5, 4, 3, 2, 1, 0'
    assert obtener_cuenta_atras(0) == '0'
    assert obtener_cuenta_atras(1) == '1, 0'
    with pytest.raises(ValueError):
        obtener_cuenta_atras(-5)
    with pytest.raises(ValueError):
        obtener_cuenta_atras("abc")