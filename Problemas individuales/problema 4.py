#Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
#pantalla la suma de todos los enteros desde 1 hasta N

# Solicitamos al usuario que digite un número entero positivo
N = int(input("Introduce un entero positivo: "))

# Condicionamos el valor a positivo
if N > 0:
    # Calculamos la suma 
    suma = sum(range(1, N + 1))
    
    print(f"La suma de todos los enteros desde 1 hasta {N} es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")
