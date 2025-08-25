# 1. Estructura de datos base: un diccionario vacío para los estudiantes
estudiantes = {}

# --- Funciones para cada opción del menú ---

def agregar_estudiante():
    """Agrega un nuevo estudiante al diccionario."""
    print("\n--- Agregar nuevo estudiante ---")
    id_estudiante = input("Ingrese el ID del estudiante (ej. A003): ").upper()

    # Validación: Verificar si el ID ya existe
    if id_estudiante in estudiantes:
        print(f"Error: El ID '{id_estudiante}' ya existe. Intente con otro.")
        return

    nombre = input("Ingrese el nombre completo: ")
    
    # Validación: La edad debe ser un número
    try:
        edad = int(input("Ingrese la edad: "))
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    calificaciones_str = input("Ingrese las calificaciones separadas por comas (ej. 85,90,75): ")
    
    # Validación: Las calificaciones deben ser números
    try:
        calificaciones = [int(c) for c in calificaciones_str.split(',')]
    except ValueError:
        print("Error: Las calificaciones deben ser números enteros.")
        return

    estudiantes[id_estudiante] = {
        "nombre": nombre,
        "edad": edad,
        "calificaciones": calificaciones
    }
    print(f"Estudiante con ID '{id_estudiante}' agregado exitosamente.")

def mostrar_estudiantes():
    """Muestra todos los estudiantes con su información."""
    print("\n--- Lista de estudiantes ---")
    if not estudiantes:
        print("No hay estudiantes registrados. Agregue uno usando la opción 1.")
    else:
        for id, info in estudiantes.items():
            if info["calificaciones"]:
                promedio = sum(info["calificaciones"]) / len(info["calificaciones"])
            else:
                promedio = 0
            print(f"ID: {id} | Nombre: {info['nombre']} | Edad: {info['edad']} | Promedio: {promedio:.2f}")

def calcular_promedio():
    """Calcula el promedio de un estudiante por su ID."""
    print("\n--- Calcular promedio de estudiante ---")
    id_estudiante = input("Ingrese el ID del estudiante: ").upper()
    
    if id_estudiante in estudiantes:
        calificaciones = estudiantes[id_estudiante]["calificaciones"]
        if calificaciones:
            promedio = sum(calificaciones) / len(calificaciones)
            print(f"El promedio de {estudiantes[id_estudiante]['nombre']} es: {promedio:.2f}")
        else:
            print("El estudiante no tiene calificaciones registradas.")
    else:
        print(f"Error: No se encontró un estudiante con el ID '{id_estudiante}'.")

def eliminar_estudiante():
    """Elimina un estudiante del diccionario por su ID."""
    print("\n--- Eliminar estudiante ---")
    id_estudiante = input("Ingrese el ID del estudiante a eliminar: ").upper()
    
    if id_estudiante in estudiantes:
        del estudiantes[id_estudiante]
        print(f"Estudiante con ID '{id_estudiante}' eliminado exitosamente.")
    else:
        print(f"Error: No se encontró un estudiante con el ID '{id_estudiante}'.")

# --- Bucle principal del programa ---

def main():
    """Función principal para ejecutar el gestor de estudiantes."""
    while True:
        print("\n--- Menú de opciones ---")
        print("1. Agregar un nuevo estudiante")
        print("2. Mostrar todos los estudiantes")
        print("3. Calcular promedio de un estudiante")
        print("4. Eliminar un estudiante")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            agregar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            calcular_promedio()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()