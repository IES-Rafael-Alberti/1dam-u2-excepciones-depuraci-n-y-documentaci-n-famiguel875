def ordenar_burbuja(lista):
    """
    @type ordenar_burbuja: función
    @param lista: lista de números
    @returns: lista de números ordenada de menor a mayor
    """
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

def main():
    a = [8, 3, 1, 19, 14]
    ordenar_burbuja(a)
    print("Lista ordenada:", a)

if __name__ == "__main__":
    main()