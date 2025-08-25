import sys
import random
import string

def generar_codigo(longitud):
    """Genera un código aleatorio de la longitud especificada."""
    caracteres = string.ascii_letters + string.digits
    codigo = ''.join(random.choice(caracteres) for _ in range(longitud))
    return codigo

def main():
    """
    Función principal que procesa los argumentos de línea de comandos.
    Espera 2 argumentos: cantidad_de_codigos y longitud_del_codigo.
    """
    try:
        if len(sys.argv) != 3:
            print("Uso: python generador_codigos.py <cantidad_de_codigos> <longitud_del_codigo>")
            print("Ejemplo: python generador_codigos.py 5 8")
            return

        cantidad_codigos = int(sys.argv[1])
        longitud_codigo = int(sys.argv[2])
        
        if cantidad_codigos <= 0 or longitud_codigo <= 0:
            print("Error: La cantidad y la longitud deben ser números positivos.")
            return

        print(f"Generando {cantidad_codigos} códigos de acceso de {longitud_codigo} caracteres cada uno:")
        
        for i in range(cantidad_codigos):
            codigo_generado = generar_codigo(longitud_codigo)
            print(f"Código {i+1}: {codigo_generado}")

    except ValueError:
        print("Error: Los argumentos deben ser números enteros.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()