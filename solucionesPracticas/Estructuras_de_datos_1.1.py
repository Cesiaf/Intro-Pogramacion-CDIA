'''
Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo)
no repetidas, guardarlos en una lista y mostrarlos.
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

# Imprimir los nombres ingresados
print("\nLos nombres ingresados son:")
for nombre in nombres:
    print(nombre)