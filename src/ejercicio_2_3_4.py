def obtener_numero_entero():
    try:
        numero = int(input("Ingrese un número entero: "))
        return numero
    except ValueError:
        raise ValueError("La entrada no es correcta. Por favor, ingrese un número entero.")

def main():
    try:
        numero = obtener_numero_entero()
        print(f"Ha ingresado el número {numero}.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()