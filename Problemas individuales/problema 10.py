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
