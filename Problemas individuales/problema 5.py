#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

# Solicitamos al usuario los datos de los shows musicales vistos
num_shows = int(input("¿Cuántos shows musicales has visto en el último año? "))

# Comprobamos la condicional de > 3
resultado = num_shows > 3

# Mostramos el resultado
print(resultado)
