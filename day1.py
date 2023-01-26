"""
~Paso 1 Leer el Archivo~
**PENDIENTE** Paso 2 Guardar cada linea en un string
**PENDIENTE** Paso 3 Detectar string iterando y guardar todos los items anteriores en una sub-lista

"""

"""" SOLUCION PAUSADA

# from itertools import groupby

listaDeNumeros = []
listaAgrupada = []
# w = "\n"


with open('input.txt') as file:
    for line in file:

        # listaDeNumeros.append(line.splitlines()) 
        
### listaAgrupada = [list(group) for key, group in groupby(listaDeNumeros, lambda x: x == w) if not key]   
print(listaDeNumeros)
"""



### V1: Perfecto funciona, tener una lista con todos los elementos y newline al final de cada conjunto.
## ME quedo aca
### This is trivial to do using list append through iteration (in a for loop) OR List comprehension


listaDeNumeros = []
listaAgrupada = []

with open('input.txt') as f:
    listaDeNumeros = f.read().splitlines()
  
print(listaDeNumeros)




### V2: esto convierte a todo el texto en un string gigantezco separado por comas. donde el newline sigue ahi 
"""from itertools import groupby

listaDeNumeros = []
listaAgrupada = []

with open('input.txt') as file:
    #listaDeNumeros = file.read().split()
    listaDeNumeros = file.read().replace('\n', ',') ## esto convierte a todo el texto en un string gigantezco separado por comas. donde el newline sigue ahi    
    [[str(x) for x in ss.split(',')] for ss in listaDeNumeros.split('\n')]
print(listaDeNumeros)"""


