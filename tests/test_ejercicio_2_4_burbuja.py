from src.ejercicio_2_4_burbuja import ordenar_burbuja

def test_ordenar_burbuja():
    # Caso general
    lista = [8, 3, 1, 19, 14]
    ordenar_burbuja(lista)
    assert lista == [1, 3, 8, 14, 19]

    # Lista ya ordenada
    lista = [1, 2, 3, 4, 5]
    ordenar_burbuja(lista)
    assert lista == [1, 2, 3, 4, 5]

    # Lista en orden descendente
    lista = [5, 4, 3, 2, 1]
    ordenar_burbuja(lista)
    assert lista == [1, 2, 3, 4, 5]

    # Lista con elementos duplicados
    lista = [5, 3, 1, 5, 2]
    ordenar_burbuja(lista)
    assert lista == [1, 2, 3, 5, 5]

    # Lista vacía
    lista = []
    ordenar_burbuja(lista)
    assert lista == []