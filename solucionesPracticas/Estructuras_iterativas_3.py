'''
Pedir que el usuario ingrese (input) nombre de personas y 
mostrarlos hasta que el valor de lo que ingresa sea “fin”
'''

while True:
    name = input("Ingrese un nombre, para finalizar la lista ingrese FIN: ").strip().lower()
    print (name)
    if name == "fin":
        break