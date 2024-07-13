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
