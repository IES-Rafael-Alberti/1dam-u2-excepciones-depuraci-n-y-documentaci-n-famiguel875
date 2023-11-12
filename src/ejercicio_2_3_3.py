def obtener_cuenta_atras(numero):
    if numero < 0:
        raise ValueError("El número debe ser positivo.")
    return ", ".join(map(str, range(numero, -1, -1)))

def main():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            countdown = obtener_cuenta_atras(numero)
            print(countdown)
            break
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()