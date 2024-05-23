'''
Eliminar la tercer y la última persona de la lista del ejercicio 1,
luego ordenar la lista y mostrarlo
'''
# Crear la lista para guardar los nombres
nombres = []

# Solicitar 10 nombres no repetidos y guardarlos en la lista
for i in range(10):
    nombre = input(f"Ingrese el nombre número {i+1} para agregar a la lista: ").strip().capitalize()
    while nombre in nombres:
        print(f"El nombre {nombre}, ya ha sido ingresado, ingrese otro nombre")
        nombre = input(f"Ingrese el nombre número {i+1} para agregar a la lista: ").strip().capitalize()
    nombres.append(nombre)

# Eliminar la tercer y la última persona de la lista
del nombres[2]
del nombres[-1]

# Ordenar la lista
nombres.sort()

# Mostrar la lista ordenada
print("\nLista de nombres final:")
for nombre in nombres:
    print(nombre)