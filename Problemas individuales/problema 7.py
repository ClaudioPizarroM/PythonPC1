#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

# Solicitamos al usuario que introduzca dos números
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

# Para mostrar el menú usaré un bucle principal para que el programa solo se acabe cuando el usuario eliga cerrarlo
while True:
    print("\nSelecciona una opción:")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta (primer número menos segundo número)")
    print("3. Mostrar la multiplicación de los dos números")
    print("0. Salir")

    opcion = input("¿Qué opción eliges? ")

    if opcion == "1":
        # Calcula la suma de los dos números
        resultado = num1 + num2
        print(f"La suma de {num1} y {num2} es: {resultado}")
    elif opcion == "2":
        # Calcula la resta de los dos número en órden
        resultado = num1 - num2
        print(f"La resta de {num1} menos {num2} es: {resultado}")
    elif opcion == "3":
        # Calcula la multiplicación de los dos números
        resultado = num1 * num2
        print(f"La multiplicación de {num1} y {num2} es: {resultado}")
    elif opcion == "0":
        # Salir del programa
        print("Gracias por usar el programa. ¡Esperamos que vuelvas pronto!")
        break
    else:
        # Opción inválida
        print("Opción no válida. Por favor, elige una opción del menú.")
