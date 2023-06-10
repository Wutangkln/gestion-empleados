
def mostrar_menu_inicio():
    menu = '''
---------- Menu -----------

1. Iniciar sesion
2. Registrarse
3. Salir

---------------------------
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
    while True:
            tipo_perfil = input("Ingresa el tipo de perfil [administrador, normal]: ")
            
            if tipo_perfil in ["administrador", "normal"]:
                break
            else:
                print("Debes ingresar alguna de las opciones indicadas. intentalo otra vez.")

    print("\n-----------------------------")

    return nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil

def mostrar_menu_gestion():
    menu = '''

--- Gestion de empleados ---

1. Lista de empleados
2. Agregar empleado
3. Eliminar un empleado
4. Actualizar un empleado
5. Crear perfil a empleado
6. cerrar la sesion

----------------------------
'''
    print(menu)