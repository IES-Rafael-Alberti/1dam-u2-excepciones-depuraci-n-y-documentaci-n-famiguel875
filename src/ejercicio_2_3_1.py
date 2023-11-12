def anios_cumplidos(edad):
    return [i for i in range(1, edad + 1)]

def main():
    try:
        edad = int(input("Ingrese su edad: "))
        print(anios_cumplidos(edad))
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()