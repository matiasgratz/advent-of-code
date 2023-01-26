"""
~Paso 1 Leer el Archivo~
**PENDIENTE** Paso 2 Guardar cada linea en un string
**PENDIENTE** Paso 3 Detectar string iterando y guardar todos los items anteriores en una sub-lista

"""

# from itertools import groupby

listaDeNumeros = []
listaAgrupada = []
# w = "\n"


with open('input.txt') as file:
    for line in file:

        # listaDeNumeros.append(line.splitlines()) 
        
### listaAgrupada = [list(group) for key, group in groupby(listaDeNumeros, lambda x: x == w) if not key]   
print(listaDeNumeros)