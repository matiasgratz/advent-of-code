import re
# Inicializar lista para almacenar el primer y último número de cada línea
resultados = []

# Solucion al 1.2
def convertir_numeros(texto):
    mapeo_numeros = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    # Ordenar las palabras de izquierda a derecha
    palabras_ordenadas = sorted(mapeo_numeros.keys(), key=lambda x: texto.find(x))

    # Realizar el reemplazo
    for palabra in palabras_ordenadas:
        texto = texto.replace(palabra, mapeo_numeros[palabra])
    
    return texto

# Nombre del archivo de entrada
nombre_archivo_entrada = 'input.txt'

try:
    # Leer el contenido del archivo
    with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    # Convertir números en cada línea
    lineas_convertidas = [convertir_numeros(linea) for linea in lineas]

    # Imprimir o guardar el resultado
    for linea_convertida in lineas_convertidas:
        print(linea_convertida)

    # Opción: Guardar el resultado en un nuevo archivo
    nombre_archivo_salida = 'input_converted.txt'
    with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo_salida:
        archivo_salida.writelines(lineas_convertidas)

    print(f"Contenido convertido y guardado en {nombre_archivo_salida}")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo_entrada}' no fue encontrado.")
except Exception as e:
    print(f"Se produjo un error: {e}")




# Abrir el archivo en modo lectura
with open("input_converted.txt", 'r') as archivo:
    # Iterar a través de las líneas en el archivo
    for linea in archivo:
        # Inicializar cadena para los números de la línea actual
        numeros_linea = ''

        # Iterar a través de los caracteres en la línea
        for caracter in linea:
            if caracter.isdigit():
                # Si el caracter es un dígito, agregar a la cadena
                numeros_linea += caracter

        # Obtener el primer y último número de la línea y agregarlos a la lista de resultados
        # A la lista de resultados le agrego, la union de los dos numeros.
        if numeros_linea:
            resultados.append("".join(map(str, (numeros_linea[0], numeros_linea[-1]))))
# Imprimir la lista resultante
# Mapeo a una lista nueva, convierto previamente en int, y sumo.
print("Lista con el primer y último número de cada línea, sumado:",  sum(map(int, resultados)))
