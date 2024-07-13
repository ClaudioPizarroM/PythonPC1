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
