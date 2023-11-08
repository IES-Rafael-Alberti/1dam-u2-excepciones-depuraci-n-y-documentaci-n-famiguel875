def main():
    try:
        edad = int(input("Por favor, ingrese su edad: "))
        for i in range(1, edad + 1):
            if i == 1:
                print("Has cumplido", i, "año")
            else:
                print("Has cumplido", i, "años")
    except ValueError:
        print("Por favor, ingrese una edad válida (número entero).")
        raise ValueError

if __name__ == "__main__":
    main()