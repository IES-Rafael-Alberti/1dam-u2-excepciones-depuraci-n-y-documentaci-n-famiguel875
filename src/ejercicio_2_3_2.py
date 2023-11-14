def obtener_impares_hasta_n(numero):
    if numero <= 0:
        raise ValueError("El número debe ser positivo.")
    return [str(x) for x in range(1, numero + 1) if x % 2 != 0]

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        impares = obtener_impares_hasta_n(numero)
        print(", ".join(impares))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()