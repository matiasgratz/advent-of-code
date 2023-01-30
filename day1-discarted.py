# IT LIVES

from itertools import groupby

with open("input.txt") as f:
    data = f.read().splitlines()
    result = [list(v) for k,v in groupby(data, key=str.isdigit)] #-Convierte a lista de listas.
    # Busco filtrar de la nested list las listas vacias
        #listaSinVacias = list(filter(lambda x: (x == ' ') , result))
        #listaSinVacias2 = [x for x in result if x != '\n']
        #listaSinVacias3 = [x for x in result if x]
            # Nada funciona, será por itertools?
    # Para luego poder usar la funcion de abajo que convierte los strings a enteros
    #nuevaLista = [int(g) for g in data]

print(result)

""" # Para la suma
# Python3 program to Column wise sum of nested list
 
def column_sum(lst):
     
    return list(map(sum, zip(*lst)))
     
# Driver code
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(column_sum(lst))

"""
