contrasena_correcta = input("Ingrese la contraseña correcta: ")  # Reemplaza con tu contraseña secreta

def main():
    try:
        contrasena = input("Ingrese la contraseña: ")
        if contrasena != contrasena_correcta:
            raise NameError("Incorrect Password!!")
        else:
            print("Contraseña correcta. Acceso concedido.")
    except NameError as e:
        print(e)

if __name__ == "__main__":
    main()