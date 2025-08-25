import sys

def verificar_contrasena():
    """
    Lee las contraseñas de un archivo y verifica si una contraseña
    ingresada por el usuario es válida.
    """
    try:
        # El bloque 'with' se asegura de que el archivo se cierre correctamente
        with open('contrasenas.txt', 'r') as archivo:
            contrasenas_validas = [linea.strip() for linea in archivo]
            
        print("--- Verificador de Contraseñas ---")
        
        # Simula un 'método post' pidiendo la contraseña al usuario
        contrasena_ingresada = input("Ingrese la contraseña para verificar: ")

        # Verificar si la contraseña ingresada está en la lista de contraseñas válidas
        if contrasena_ingresada in contrasenas_validas:
            print("\n¡Login exitoso! La contraseña es válida.")
        else:
            print("\nAcceso denegado. La contraseña ingresada no es correcta.")

    except FileNotFoundError:
        print("Error: El archivo 'contrasenas.txt' no fue encontrado.")
        print("Asegúrese de que el archivo existe y está en la misma carpeta que el script.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecutar la función principal del programa
if __name__ == "__main__":
    verificar_contrasena()