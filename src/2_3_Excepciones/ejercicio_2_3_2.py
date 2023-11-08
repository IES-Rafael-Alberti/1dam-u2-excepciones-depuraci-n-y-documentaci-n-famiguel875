def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 0:
            print("El número debe ser positivo.")
        else:
            impares = [str(x) for x in range(1, numero + 1) if x % 2 != 0]
            print(", ".join(impares))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()