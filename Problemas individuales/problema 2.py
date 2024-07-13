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
