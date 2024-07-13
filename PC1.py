#PROBLEMA 1

# Escribir un programa que solicite su nombre de usuario por consola y después de que el usuario lo
# introduzca muestre por pantalla la cadena “¡Hola <nombre>!”, donde <nombre> es el nombre que el
# usuario haya introducido.

nombre = input("Bienvenido, por favor introduzca su usuario: ")
print(f"¡Hola {nombre}!")

#PROBLEMA 2

# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.


# 1. Solicitamos la información del consumo total en el restaurante.
consumo = float(input("Por favor, introduce el monto de tu consumo en el restaurante: "))

# 2. Solicitamos el porcentaje de propina que el cliente dejará
porcentaje_propina = input("¿Qué porcentaje de propina deseas dejar?: ")

# Con esta línea eliminaremos el simbolo de porcentaje en caso el cliente la haya digitado. 
porcentaje_propina = float(porcentaje_propina.strip('%'))

# 3. Calculamos la propina
propina = consumo * (porcentaje_propina / 100)

# 4. La mostramos en pantalla.
print(f"La cantidad de propina a dejar es: S/ {propina:.2f}")

#PROBLEMA 3

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta
#por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el
#peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y
#cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el
#último pedido y calcule el peso total del paquete que será enviado.

# Definimos las variables de peso de los juguetes
peso_payaso = 112
peso_muneca = 75

# Solicitamos al usuario el número de payayos vendidos
payasos_vendidos = int(input("Introduce el número de payasos vendidos: "))

# Solicitamos al usuario el número de muñecas vendidas
munecas_vendidas = int(input("Introduce el número de muñecas vendidas: "))

# Calculamos el peso total
peso_total_gramos = (payasos_vendidos * peso_payaso) + (munecas_vendidas * peso_muneca)
peso_total_kilogramos = (peso_total_gramos) / 1000

print(f"El peso total del paquete es: {peso_total_gramos} gramos")
print(f"El peso total del paquete es: {peso_total_kilogramos:.2f} kilogramos")

#PROBLEMA 4

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

#PROBLEMA 5

#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

# Solicitamos al usuario los datos de los shows musicales vistos
num_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Comprobamos la condicional de > 3
resultado = num_shows > 3

# Mostramos el resultado
print(resultado)

#PROBLEMA 6

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

    #PROBLEMA 7

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


# PROBLEMA 8

#Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
#entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
#Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
#hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
#Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
#suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
#las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
#Nota:
#Recuerde que cuando solicitamos datos a través de un input este nos devuelve un str, quizás le sea
#más fácil realizar la comparación convirtiendo los datos a float.
#Ejemplo :
#Dato ingresado: “7:30” se puede interpretar como 7.5

# Solicitamos al usuario que introduzca la hora en el formato "H:MM" o "HH:MM"
time = input("Por favor, introduzca la hora en formato H:MM o HH:MM: ")

# Usamos un metodo de cadena para luego transformar los valores de la hora ingresada
horas, minutos = time.split(":")

# Convertimos la hora y los minutos a números enteros
horas = int(horas)
minutos = int(minutos)

# Convertir la hora a formato flotante
hora_decimal = horas + minutos / 60.0

# Determinar si es hora de desayunar, almorzar o cenar
if 7.0 <= hora_decimal <= 8.0:
    print("Es la hora del desayuno.")
elif 12.0 <= hora_decimal <= 13.0:
    print("Es la hora del almuerzo.")
elif 18.0 <= hora_decimal <= 19.0:
    print("Es la hora de la cena.")
# Si no es hora de comer, no se envía nada


#PROBLEMA 9

#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a',
#'día', 'buen', 'Di'].

# Definimos una función para que el programa devuelva una lista en reversa
def invertir_lista(lista):
    # Usamos una copia para no afectar a la original y luego poder mostrarla
    lista_copia = lista.copy()
    # Utilizar el método reverse para invertir la lista
    lista_copia.reverse()
    return lista_copia

# Generamos la lista original 
lista_original = ['Di', 'buen', 'día', 'a', 'papa']

# Aplicamos la función que programamos para devolverla invertida
lista_invertida = invertir_lista(lista_original)

# Mostrar la lista invertida
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)


#PROBLEMA 10

#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5.
#lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']

# Agregamos la lista 
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminamos los elementos en las posiciones 0, 4 y 5. Lo hacemos en orden invertido ya que sino me moverá la lista y no se borrarán los correctos. 
del lista_muestra[5]
del lista_muestra[4]
del lista_muestra[0]

print("Resultado después de depuración", lista_muestra)


#PROBLEMA 11

#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4,, 5]

# Agregamos la lista con los datos originales
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Usaré una lista vacía para ir agregando los valores sin duplicados
lista_sin_duplicados = []

# Con iteración se irán agregando los valores a la nueva lista cumpliendo con la condicional de no repetirse. 
for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

# Mostrar la lista procesada
print("Lista original:", lista_original)
print("Lista sin duplicados:", lista_sin_duplicados)


#PROBLEMA 12

#La mayoría de los archivos tienen extensiones de archivo, el cual es un sufijo que comienza con un
#punto (.) al final de su nombre. Por ejemplo, los nombres de archivo para GIF terminan en .gif y los
#nombres de archivo para JPEG terminan en .jpg o .jpeg. Mientras que en los sistemas operativos
#como Windows, el tipo de archivo le sirve al computador abrir el archivo en el formato apropiado, en
#la web esto es distinto. Los navegadores web, por el contrario, se basan en tipos de medios,
#anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en
#la web.
#Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
#archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
#importar el uso de mayúsculas y minúsculas) :
#- .gif
#- .jpg
#- .jpeg
#- .png
#- .pdf
#- .txt
#- .zip
#Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
#ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
#Ejemplos:
#Nombre Archivo: happy.jpg Salida Esperada: image/jpeg
#Nombre Archivo: document.pdf Salida Esperada: application/pdf
#Para conocer los tipos MIME a utilizar, puede revisar el siguiente enlace.
#Nota:
#- El empleo de diccionarios podría ayudar con esta tarea.
#- El uso de métodos de cadena sería muy útil al momento de separar el nombre del archivo de
#su extensión.

#Establecemos una función para obtener la extensión correspondiente al nombre del archivo
def obtener_tipo_mime(nombre_archivo):
    # Homologamos el nombre a minuscula para cualquier nombre que digiten
    nombre_archivo = nombre_archivo.lower()

    # Usamos un diccionario para las extesiones MIME
    extensiones_mime = {
        'gif': 'image/gif',
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'pdf': 'application/pdf',
        'txt': 'text/plain',
        'zip': 'application/zip'
    }

    # Obtenemos la extensión del archivo usando condicionales 
    if '.' in nombre_archivo:
        extension = nombre_archivo.rsplit('.', 1)[1] 
        if extension in extensiones_mime:
            return extensiones_mime[extension]

    # En caso no esté en nuestro listado MIME
    return 'application/octet-stream'

# Solicitar al usuario que ingrese el nombre del archivo
nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener el tipo MIME correspondiente
tipo_mime = obtener_tipo_mime(nombre_archivo)

# Mostrar el resultado
print(f"Tipo MIME para '{nombre_archivo}': {tipo_mime}")