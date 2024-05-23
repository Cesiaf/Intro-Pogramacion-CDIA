'''
Desarrollar en Python un módulo que gestione una agenda telefónica en un 
diccionario de Python utilizando los recursos ya vistos 
(variables, input, print, if, if - else, while, for) que consideren adecuados
para cada uno de estos casos:

Mostrar al usuario un menú de opciones

Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono).
Esta opción debe agregar al diccionario a la persona que el usuario ingrese

Opción 2: Modificar una persona: dado su dni debe buscar la persona y
preguntar si desea cambiar los demás campos de la persona, 
cambiando los que quiera.

Opción 3: Eliminar una persona del diccionario. Elimina según el DNI

Opción 4: Mostrar todos la agenda

Opción 5: Salir
'''

# Crear el Diccionario "Agenda"
Agenda =  {}

# Creae el Menú de Opciones a mostrar
while True:
    print("\nMenú de opciones:")
    print("1. Agregar una persona")
    print("2. Modificar una persona")
    print("3. Eliminar una persona")
    print("4. Mostrar toda la agenda")
    print("5. Salir")

    # Seleccionar opción del usuario
    opcion = input("Seleccione una opción: ")

    # Efectuar las operaciones según la opción elegida
    # Opción para Agregar a una persona nueva
    if opcion == "1":
        print("\nAgregar a una persona")

        # Agregar Datos a variables
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        dni = input("DNI: ")
        email = input("E-mail: ")
        telefono = input("Teléfono: ")

        # Guardar variables en diccionario como valor para sus respectivas claves
        Agenda[dni] = {"apellido": apellido, "nombre": nombre, "email": email, "telefono": telefono}
        print("\nPersona Agregada con Éxito")

    # Opción para Modificar un contacto agendado previamente
    if opcion == "2":
        print("\n Modificar una persona")

        # Buscar a la persona en diccionario "Agenda" por su DNI
        dni = input("Ingrese el DNI de la persona que desea modificar: ")

        # Se ejecuta si la persona está agendada
        if dni in Agenda:
            
            # Mostrar los datos de la persona encontrada
            print ("\nPersona Encontrada")
            print("Apellido: ", Agenda[dni]["apellido"])
            print("Nombre: ", Agenda[dni]["nombre"])
            print("E-mail: ", Agenda[dni]["email"] )
            print("Teléfono: ", Agenda[dni]["telefono"])

            # Preguntar si se desea modificar el contacto
            opt = input("¿Desea modificar este contacto? Sí/No: ").strip().lower()

            # Guardar los nuevos datos en variables
            if opt in ["si", "sí"]:
                apellido = input("Nuevo apellido (deje vacío si no desea cambiar): ")
                nombre = input("Nuevo nombre (deje vacío si no desea cambiar): ")
                email = input("Nuevo email (deje vacío si no desea cambiar): ")
                telefono = input("Nuevo número de teléfono (deje vacío si no desea cambiar): ")
                
                # Guardar los datos como valor para sus respectivas claves en Agenda
                if apellido:
                    Agenda[dni]["apellido"] = apellido
                if nombre:
                    Agenda[dni]["nombre"] = nombre
                if email:
                    Agenda[dni]["email"] = email
                if telefono:
                    Agenda[dni]["telefono"] = telefono
                # Mostrar los datos modificados
                print("Datos modificados.")
            else:
            # Avisar que no se ha modificado ningún dato
                print("No se ha modificado ningún dato.")

        # Mostrar aviso de que no hay ninguna persona agendada con el DNI brindado
        else:
            print("La persona con ese DNI no está en la agenda.")   

    #Opción para eliminar una persona  
    elif opcion == "3":
        print("\nEliminar una persona:")
        dni = input("Ingrese el DNI de la persona que desea eliminar de la agenda: ")
        
        # Buscar a la persona indicada por el DNI brindado y eliminarla de la Agenda
        if dni in Agenda:
            del Agenda[dni]  
            print("Persona eliminada de la agenda.")
        # Dar aviso si la persona no se encuentra registrada en la agenda
        else:
            print(f"La persona con DNI {dni} no está registrada en la agenda.")
    # Opción para mostrar todos la agenda
    elif opcion == "4":
        print("\nMostrar toda la agenda")

        #Imprimir la agenda completa
        for dni, datos in Agenda.items():
            print("\nDNI:", dni)
            print("Apellido:", datos["apellido"])
            print("Nombre:", datos["nombre"])
            print("Email:", datos["email"])
            print("Teléfono:", datos["telefono"])
    
    # Opción para Salir
    elif opcion == "5":
         print("\nSaliendo...")
         break


