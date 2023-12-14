def convertir_numeros(input_text):
    mapeo_numeros = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9}
    
    for palabra, numero in mapeo_numeros.items():
        input_text = input_text.replace(palabra, str(numero))
    
    return input_text

# Solicitar input al usuario
entrada_usuario = input("Ingrese un texto con números del uno al nueve en palabras: ")

# Convertir números en el input
resultado_convertido = convertir_numeros(entrada_usuario)

# Imprimir el resultado
print("Resultado convertido:", resultado_convertido)