def procesar_archivos():
    """Lee estudiantes.txt, calcula el promedio y genera reporte.txt."""
    try:
        # Intenta abrir y leer el archivo de estudiantes
        with open('estudiantes.txt', 'r') as archivo_lectura:
            lineas = archivo_lectura.readlines()
            
            calificaciones = []
            contenido_original = ""
            
            for linea in lineas:
                contenido_original += linea
                partes = linea.strip().split(',')
                if len(partes) == 2:
                    try:
                        calificacion = int(partes[1])
                        calificaciones.append(calificacion)
                    except ValueError:
                        print(f"Error: La calificación en la línea '{linea.strip()}' no es un número válido. Se omitirá.")
                else:
                    print(f"Error: Formato de línea incorrecto en '{linea.strip()}'. Se omitirá.")
            
            # Calcular el promedio general
            if calificaciones:
                promedio = sum(calificaciones) / len(calificaciones)
                linea_promedio = f"Promedio general: {promedio:.2f}"
            else:
                promedio = 0
                linea_promedio = "Promedio general: No se encontraron calificaciones válidas."

            # Escribir el nuevo archivo de reporte
            with open('reporte.txt', 'w') as archivo_escritura:
                archivo_escritura.write(contenido_original)
                archivo_escritura.write(linea_promedio + '\n')

            print("Reporte generado exitosamente.")
            print(f"El promedio general es: {promedio:.2f}")

    except FileNotFoundError:
        print("Error: El archivo 'estudiantes.txt' no fue encontrado. Asegúrate de que existe en la misma carpeta.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def agregar_estudiante():
    """Permite al usuario agregar un nuevo estudiante al archivo."""
    print("\n--- Agregar nuevo estudiante ---")
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        calificacion = int(input(f"Ingrese la calificación de {nombre}: "))
        with open('estudiantes.txt', 'a') as archivo_agregar:
            archivo_agregar.write(f"\n{nombre},{calificacion}")
        print(f"Estudiante '{nombre}' agregado exitosamente.")
    except ValueError:
        print("Error: La calificación debe ser un número entero.")
    except FileNotFoundError:
        print("Error: El archivo 'estudiantes.txt' no fue encontrado.")

# Bucle principal del programa
def main():
    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Procesar calificaciones y generar reporte")
        print("2. Agregar un nuevo estudiante")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            procesar_archivos()
        elif opcion == '2':
            agregar_estudiante()
        elif opcion == '3':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()