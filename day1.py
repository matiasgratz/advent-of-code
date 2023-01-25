"""
El algoritmo es el siguiente:
Necesito una funcion, que en base al input (lista de numeros, separados de enter, con el blank de centinela). Ponga todos esos valores sumados
En un array o (lista)? y luego de ese array consulto cual es el mayor comparando. (algoritmo2).
"""

"""
Paso 1 Leer el Archivo
Paso 2 Guardar cada linea en un string
Paso 3 

Separar listas en lista mas chicas con un delimitador
Leer el archivo a lineas
Lista de listas

"""
with open('input.txt') as file:
    for line in file:
        print(line.splitlines())
        