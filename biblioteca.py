def agregar_contacto(agenda, nombre, telefono, email):
    """Agrega un nuevo contacto a la agenda."""
    if nombre in agenda:
        print("El contacto ya existe.")
    else:
        agenda[nombre] = {'telefono': telefono, 'email': email}
        print(f"Contacto '{nombre}' agregado.")

def mostrar_contactos(agenda):
    """Muestra todos los contactos."""
    if not agenda:
        print("No hay contactos en la agenda.")
    else:
        for nombre, info in agenda.items():
            print (f"Nombre: {nombre}, Teléfono")
