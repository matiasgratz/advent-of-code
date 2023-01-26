# IT LIVES
from itertools import groupby

with open("input.txt") as f:
    #Primero tengo que convertir los strings a int antes de que se metan en lista de listas porque si no, no se puede luego.
    data = f.read().splitlines()
    enNumeros = [ int(x) for x in data.split() ] 
# result = [list(v) for k,v in groupby(data, key=str.isdigit)] - Convierte a lista de listas.

print(enNumeros)

"""
# Python3 program to Column wise sum of nested list
 
def column_sum(lst):
     
    return list(map(sum, zip(*lst)))
     
# Driver code
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(column_sum(lst))

"""
