'''
En un nuevo diccionario llamado familia guardar 4 personas, 
cada una de ellas con los mismos 5 datos 
(nombre, apellido, dni, email, fecha de nacimiento)
'''
# Crear un diccionario para almacenar los datos de la familia
familia = {}

# Solicitar y almacenar los datos de las 4 personas en "familia"
for i in range(1, 5):
    print(f"Ingrese los datos de la persona {i}:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    email = input("Correo electrónico: ")
    fecha_nacimiento = input("Fecha de nacimiento (en formato DD/MM/YYYY): ")

    # Almacenar los datos de la persona en el diccionario "familia"
    familia[f"persona_{i}"] = {"nombre": nombre, "apellido": apellido, "dni": dni, "email": email, "fecha_nacimiento": fecha_nacimiento}

# Mostrar los datos de la familia
print("\nDatos de la familia:")
for nombre_persona, datos_persona in familia.items():
    print(f"\n{nombre_persona}:")
    for clave, valor in datos_persona.items():
        print(f"{clave}: {valor}")
