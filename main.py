# main.py

# Importar las librerías personales
import saludo
import matematicas
import datos

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú de Opciones ---")
    print("1. Saludar")
    print("2. Realizar operaciones matemáticas")
    print("3. Ver información de la aplicación")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    """Función principal que ejecuta el programa."""
    nombre_usuario = input("Por favor, ingrese su nombre: ")
    print(saludo.bienvenida(nombre_usuario))

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            print(saludo.despedida())
        elif opcion == '2':
            # Solicitar números para las operaciones
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                print(f"\nLa suma de {num1} y {num2} es: {matematicas.sumar(num1, num2)}")
                print(f"La multiplicación de {num1} y {num2} es: {matematicas.multiplicar(num1, num2)}")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese solo números.")
        elif opcion == '3':
            print(f"Información de la aplicación: {datos.obtener_info_app()}")
            print(f"Valor de PI (desde la librería): {matematicas.PI}")
        elif opcion == '4':
            print(saludo.despedida())
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()