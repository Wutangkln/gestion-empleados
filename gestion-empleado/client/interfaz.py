
def mostrar_menu_inicio():
    menu = '''
---------- Menu -----------

1. Iniciar sesion
2. Registrarse
3. Salir

---------------------------
'''

    print(menu)

def mostrar_menu_gestion():
    menu = '''
--- Gestion de empleados ---

1. Lista de empleados
2. Actualizar un empleado
3. Eliminar un empleado
4. cerrar el programa

----------------------------
'''

    print(menu)

def obtener_opcion():
    opcion = input("\n Escoge una opcion: ")
    
    return opcion

def menu_inicio_sesion():
    print("\n------- Inicio Sesion -------")

    nombre_usuario = input("Escoge el nombre de usuario: ")
    clave = input("Escoge una clave de acceso: ")

    print("\n-----------------------------")

    return nombre_usuario, clave

def menu_registro():
    print("\n--------- Registro ---------")

    nombre_usuario = input("Escoge el nombre de usuario: ")
    rut_empleado = input("Ingresa tu rut: ")
    clave = input("Escoge una clave de acceso: ")
    clave_repetida = input("Ingresa la clave de acceso otra vez: ")
    tipo_perfil = input("Ingresa el tipo de perfil [administrador, normal]: ")

    print("\n-----------------------------")

    return nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil