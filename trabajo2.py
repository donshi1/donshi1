import numpy as np

# Definir dos matrices (arrays de NumPy)
# Puedes cambiar los valores si quieres
matriz_A = np.array([[1, 2], [3, 4]])
matriz_B = np.array([[5, 6], [7, 8]])

print("Matriz A:")
print(matriz_A)
print("\nMatriz B:")
print(matriz_B)

# --- Operaciones ---

# 1. Suma
print("\n--- Suma de Matrices (A + B) ---")
suma = matriz_A + matriz_B
print(suma)

# 2. Resta
print("\n--- Resta de Matrices (A - B) ---")
resta = matriz_A - matriz_B
print(resta)

# 3. Multiplicación (producto punto o matricial)
# El operador '@' es la forma moderna para el producto matricial.
print("\n--- Multiplicación Matricial (A @ B) ---")
multiplicacion = matriz_A @ matriz_B
print(multiplicacion)

# Si usas el operador '*' se hace una multiplicación elemento a elemento
print("\n--- Multiplicación elemento a elemento (A * B) ---")
multiplicacion_elemento = matriz_A * matriz_B
print(multiplicacion_elemento)

# 4. Transposición
print("\n--- Transposición de la Matriz A (A^T) ---")
transposicion_A = matriz_A.T
print(transposicion_A)
