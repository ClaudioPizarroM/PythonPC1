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
