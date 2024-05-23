'''
Guardar en un diccionario los datos de una persona: 
nombre, apellido, dni, email, fecha de nacimiento.
'''
# Crear diccionario vacío
persona = {}

# Ingresar Datos de la persona
persona["nombre"]= input("Ingrese nombre de la persona: ")
persona["apellido"]= input("Ingrese apellido de la persona: ")
persona["DNI"]= input("Ingrese DNI de la persona: ")
persona["email"]= input("Ingrese E-mail de la persona: ")
persona["fecha_nacimiento"]= input("Ingrese Fecha de Nacimiento de la persona (en formato DD/MM/YYYY): ")

# Imprimir Diccionario con datos

print ("\nDatos de la persona:")
       
for clave, valor in persona.items():
    print(f"{clave}: {valor}")