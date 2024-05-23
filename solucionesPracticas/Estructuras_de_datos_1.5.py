'''
Guardar en una tupla los primeros n números pares. El valor de n que lo ingrese 
el usuario (input). Luego mostrar los datos de la tupla.
'''
# Definir n
n=int((input("Ingrese el rango de números que desea recorrer: ")))

# Creae una lista para guardar los números pares
pares = []

# Calcular y guardar los primeros n pares en la tupla "numeros pares"
for i in range(1,n+1):
    if i % 2 == 0:
        pares.append(i)

# Crear una tupla a partir de la lista de elementos
numeros_pares = tuple(pares)
 
print("Los primeros", n, "números pares son:", numeros_pares)