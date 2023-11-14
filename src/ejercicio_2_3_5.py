def verificar_contrasena(contrasena_ingresada, contrasena_correcta):
    if contrasena_ingresada != contrasena_correcta:
        raise NameError("¡Contraseña incorrecta!")

def main():
    contrasena_correcta = input("Ingrese la contraseña correcta: ")

    try:
        contrasena = input("Ingrese la contraseña: ")
        verificar_contrasena(contrasena, contrasena_correcta)
        print("Contraseña correcta. Acceso concedido.")
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()