import pytest

from src.ejercicio_2_3_5 import verificar_contrasena

def test_verificar_contrasena():
    contrasena_correcta = "contraseña123"
    verificar_contrasena("contraseña123", contrasena_correcta)  
    with pytest.raises(NameError):
        verificar_contrasena("contraseña456", contrasena_correcta)