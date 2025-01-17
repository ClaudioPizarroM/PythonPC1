#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

# Solicita al usuario que introduzca la edad del cliente
edad = int(input("Introduce la edad del cliente: "))

# Verificamos si la edad ingresada es positiva o cero
if edad < 0:
    print("Por favor, introduce una edad válida (mayor o igual a cero).")
else:
    # Determina el precio de la entrada según la edad del cliente
    if edad < 4:
        precio = 0
    elif 4 <= edad <= 18:
        precio = 5
    else:
        precio = 10

    # Muestra el precio de la entrada
    print(f"El precio de la entrada es: ${precio}")
