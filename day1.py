"""
~Paso 1 Leer el Archivo~
**PENDIENTE** Paso 2 Guardar cada linea en un string
**PENDIENTE** Paso 3 Detectar string iterando y guardar todos los items anteriores en una sub-lista

"""
with open('input.txt') as file:
    for line in file:
        print(line.splitlines())
        