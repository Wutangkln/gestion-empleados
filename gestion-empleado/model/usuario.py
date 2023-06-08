from .conexion import Conexion

import mysql.connector

class Usuario:
    def __init__(self, nombre_usuario, clave, tipo_perfil):
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.tipo_perfil = tipo_perfil

def validar_credenciales(nombre_usuario, clave):
    
    if nombre_usuario == "admin" and clave == "admin":
        print("\nBienvenido administrador.")
        return True

    # db_conexion = Conexion()

    # Codigo para validar credenciales

    # db_conexion.cerrar_conexion()

def registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil):
    if clave != clave_repetida:
        return "Las claves de acceso no coinciden."
    
    try:
        conexion = Conexion()

        conexion.cursor.execute("SELECT * FROM empleados WHERE rut = %s", (rut_empleado,))
        resultado = conexion.cursor.fetchone()

        if resultado is None:
            conexion.cerrar_conexion()
            return "El Rut ingresado no corresponde a un empleado valido."
        
        conexion.cursor.execute("SELECT * FROM perfil WHERE usuario = %s", (nombre_usuario,))
        resultado = conexion.cursor.fetchone()

        if resultado is None:
            conexion.cerrar_conexion()
            return "El nombre de usuario ya se encuentra en uso."
        
        conexion.cursor.execute("INSERT INTO perfil VALUES(%s, %s, %s)",(nombre_usuario, clave, tipo_perfil))
        conexion.conexion.commit()
        conexion.cerrar_conexion()

        return "El usuario se ha registrado con exito."

    except mysql.connector.Error as err:
        print(f"Algo salio mal: {err}")
        return "Ocurrio un error al intentar registrar al usuario."
