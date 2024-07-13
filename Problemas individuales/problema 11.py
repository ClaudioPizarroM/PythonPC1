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
