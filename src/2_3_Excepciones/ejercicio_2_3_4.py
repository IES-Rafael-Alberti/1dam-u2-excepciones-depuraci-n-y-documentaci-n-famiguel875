def main():
    try:
        numero = int(input("Ingrese un número entero: "))
    except ValueError:
        print("La entrada no es correcta")

if __name__ == "__main__":
    main()