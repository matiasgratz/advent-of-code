#OLD
### V1: Perfecto funciona, tener una lista con todos los elementos y newline al final de cada conjunto.
## ME quedo aca
### This is trivial to do using list append through iteration (in a for loop) OR List comprehension

"""
listaDeNumeros = []
listaAgrupada = []

with open('input.txt') as f:
    listaDeNumeros = f.readlines()
    listaAgrupada.append(listaDeNumeros.split())
print(listaDeNumeros)
"""



### V2: esto convierte a todo el texto en un string gigantezco separado por comas. donde el newline sigue ahi 
"""from itertools import groupby

listaDeNumeros = []
listaAgrupada = []

with open('input.txt') as file:
    #listaDeNumeros = file.read().split()
    listaDeNumeros = file.read().replace('\n', ',') ## esto convierte a todo el texto en un string gigantezco separado por comas. donde el newline sigue ahi    
    [[str(x) for x in ss.split(',')] for ss in listaDeNumeros.split('\n')]
print(listaDeNumeros)"""