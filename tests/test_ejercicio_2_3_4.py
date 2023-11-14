import pytest

from src.ejercicio_2_3_4 import obtener_numero_entero

def test_obtener_numero_entero():
    assert obtener_numero_entero() == 5
    assert obtener_numero_entero() == 0
    assert obtener_numero_entero() == -10
    with pytest.raises(ValueError):
        obtener_numero_entero("abc")