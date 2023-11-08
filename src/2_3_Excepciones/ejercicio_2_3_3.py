def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero < 0:
                print("El número debe ser positivo.")
            else:
                countdown = ", ".join(map(str, range(numero, -1, -1)))
                print(countdown)
                break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()