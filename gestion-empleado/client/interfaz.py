
def mostrar_menu_inicio():
    menu_inicio = '''
---------- Menu -----------

1. Iniciar sesion
2. Registrarse
3. Salir

---------------------------
'''

    print(menu_inicio)

def mostrar_menu_gestion():
    menu_gestion = '''

--- Gestion de empleados ---

1. Lista de empleados
2. Agregar empleado
3. Eliminar un empleado
4. Actualizar un empleado
5. Crear perfil a empleado
6. cerrar la sesion

----------------------------
'''
    print(menu_gestion)

def solicitar_dato(mensaje):
    return input(f"{mensaje}: ")

def menu_inicio_sesion():
    print("\n------- Inicio Sesion -------")
    print("si deseas volver al menu, solo debes ingresa 'cancelar'")

    nombre_usuario = solicitar_dato("Escoge el nombre de usuario")
    if nombre_usuario.lower() == "cancelar":
        return None, None

    clave = solicitar_dato("Escoge una clave de acceso")
    if clave.lower() == "cancelar":
        return None, None

    print("\n-----------------------------")

    return nombre_usuario, clave

def menu_registro():
    print("\n--------- Registro ---------")
    print("si deseas volver al menu, solo debes ingresa 'cancelar'. (solo sera valido en el primer campo.)")

    nombre_usuario = solicitar_dato("Escoge el nombre de usuario")
    if nombre_usuario.lower() == "cancelar":
        return None, None, None, None, None

    rut_empleado = solicitar_dato("Ingresa tu rut")
    clave = solicitar_dato("Escoge una clave de acceso")
    clave_repetida = solicitar_dato("Ingresa la clave de acceso otra vez")

    while True:
        tipo_perfil = solicitar_dato("Ingresa el tipo de perfil [administrador, normal]")
        if tipo_perfil in ["administrador", "normal"]:
            break
        else:
            print("Debes ingresar alguna de las opciones indicadas. intentalo otra vez.")

    print("\n-----------------------------")

    return nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil