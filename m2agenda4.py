# una ilustración para empezar
print("   ___      _            _       _   ")
print("  / ____|    | |          | |     | |  ")
print(" | |     _ _| | __ _ _ | |__| | ")
print(" | |    / ` | |/ _ \\ '\\| __/ _ \\ __|")
print(" | |___| (| | |  __/ | | | ||  __/ | ")
print("  \\____\\__,_|_|\\__|_| |_|\\_\\__|\\_|")
print("  LA GRAN AGENDA DE CARLOS")

# creación clase Contacto
class Contacto:
    # constructor de la clase 
    def __init__(self, nombre, apellido, telefono, correo, direccion):
        # los atributos 
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    # muestra detalles de clase contacto
    def mostrar_detalles(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Teléfono:", self.telefono)
        print("Correo:", self.correo)
        print("Dirección:", self.direccion)

# creación clase Agenda
class Agenda:
    # constructor de la clase
    def __init__(self):
        # la lista de contactos que se irá llenando
        self.contactos = []

    # para agregar un contacto
    def agregar_contacto(self):
        # ingresar datos contacto
        nombre = input("Ingrese el nombre del contacto: ")
        apellido = input("Ingrese el apellido del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        direccion = input("Ingrese la dirección del contacto: ")

        # crea un objeto Contacto
        contacto = Contacto(nombre, apellido, telefono, correo, direccion)

        # agrega el contacto a la lista
        self.contactos.append(contacto)

        print("El contacto ha sido agregado")

    # para modificar un contacto 
    def modificar_contacto(self):
        # ingresar nombre del contacto a modificarse
        nombre = input("Ingrese el nombre del contacto a modificar: ")

        # buscar el contacto 
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                # ingresar nuevos datos
                nuevo_nombre = input("Ingrese el nuevo nombre del contacto: ")
                nuevo_apellido = input("Ingrese el nuevo apellido del contacto: ")
                nuevo_telefono = input("Ingrese el nuevo teléfono del contacto: ")
                nuevo_correo = input("Ingrese el nuevo correo del contacto: ")
                nuevo_direccion = input("Ingrese la nueva dirección del contacto: ")

                # actualizar datos
                contacto.nombre = nuevo_nombre
                contacto.apellido = nuevo_apellido
                contacto.telefono = nuevo_telefono
                contacto.correo = nuevo_correo
                contacto.direccion = nuevo_direccion

                print("Contacto modificado ")
                return

        print("Contacto no encontrado")

    # eliminar contacto existente
    def eliminar_contacto(self):
        # ingresar nombre del contacto a eliminarse
        nombre = input("Ingrese el nombre del contacto a eliminar: ")

        # buscar el contacto 
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                # eliminar el contacto 
                self.contactos.remove(contacto)

                print("Contacto eliminado ")
                return

        print("Contacto no encontrado ")

    # buscar contactos por nombre, apellido o número de teléfono
    def buscar_contacto(self):
        # ingresar nombre, apellido o número de teléfono
        busqueda = input("Ingrese el nombre, apellido o número de teléfono del contacto a buscar: ")

        # buscar el contacto 
        for contacto in self.contactos:
            if contacto.nombre == busqueda or contacto.apellido == busqueda or contacto.telefono == busqueda:
                # Mostrar los datos del contacto
                contacto.mostrar_detalles()
                return

        print("Contacto no encontrado ")

    # para mostrar todos los contactos existentes
    def mostrar_contactos(self):
        # por si la lista de contactos está vacía
        if len(self.contactos) == 0:
            print("No hay contactos ")
        else:
            # Mostrar los detalles de cada contacto
            for contacto in self.contactos:
                contacto.mostrar_detalles()
                print()  # espacio blanco

# crear menú
agenda = Agenda()

while True:
    # menú 
    print("1. Agregar contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Buscar contacto")
    print("5. Mostrar todos los contactos")
    print("6. Salir")

    # ingresar opción 
    opcion = input("Ingrese la opción deseada: ")

    # Ejecutar la opción seleccionada
    if opcion == "1":
        agenda.agregar_contacto()
    elif opcion == "2":
        agenda.modificar_contacto()
    elif opcion == "3":
        agenda.eliminar_contacto()
    elif opcion == "4":
        agenda.buscar_contacto()
    elif opcion == "5":
        agenda.mostrar_contactos()
    elif opcion == "6":
        break
    else:
        print("No es válido, intente nuevamente")
