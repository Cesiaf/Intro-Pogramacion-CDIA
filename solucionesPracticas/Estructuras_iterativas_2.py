'''
Mostrar sólo los números pares desde 0 hasta el número ingresado (input). 
Nota: para saber si un número es par hacer i % 2 == 0)
'''

#Solicitar número final al usuario
numero_final = int(input("Mostrar números del cero al: "))

#Imprimir secuencia numérica
for i in range(0,numero_final+1):
    if i % 2 == 0:
        print (i)
