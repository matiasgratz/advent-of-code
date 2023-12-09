# Inicializar lista para almacenar el primer y último número de cada línea
resultados = []

# Abrir el archivo en modo lectura
with open("input.txt", 'r') as archivo:
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
print("Lista con el primer y último número de cada línea:",  sum(map(int, resultados)))
