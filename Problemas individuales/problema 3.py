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