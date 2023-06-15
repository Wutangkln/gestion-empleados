from .conexion import Conexion
from .empleado import Empleado

import mysql.connector
import pdb


class Usuario:
    def __init__(self, nombre_usuario, clave, tipo_perfil):
        self.nombre_usuario = nombre_usuario
        self.clave = clave
        self.tipo_perfil = tipo_perfil

    def ingresar_perfil(self, id_filtrado, rut_empleado):
        try:
            conexion = Conexion()
            conexion.cursor.execute("USE empleados")

            consulta = "SELECT * FROM perfil WHERE id_empleado = %s"
            conexion.cursor.execute(consulta, (id_filtrado,))

            resultados = conexion.cursor.fetchone()

            if resultados != None:
                print("El empleado ya tiene un perfil creado.")
            else:
                insertar_comando = "INSERT INTO perfil(nombre_usuario, clave, tipo_perfil, id_empleado) VALUES(%s, %s, %s, %s)"
                valores_empleado = (self.nombre_usuario,
                                    self.clave, self.tipo_perfil, id_filtrado)
                conexion.cursor.execute(insertar_comando, valores_empleado)

                conexion.conexion.commit()

                print("Se ha creado correctamente el perfil asociado al empleado")

        except Exception as error:
            conexion.conexion.rollback()
            print(f"Se produjo un error: {error}")

        finally:
            conexion.cerrar_conexion()


def validar_credenciales(nombre_usuario, clave):

    if nombre_usuario == "admin" and clave == "admin":
        print("\nBienvenido administrador.")

        return True, "administrador"

    conexion = Conexion()
    conexion.cursor.execute("USE empleados")

    try:
        validar_usuario = "SELECT nombre_usuario, tipo_perfil FROM perfil WHERE nombre_usuario = %s AND clave = %s"
        conexion.cursor.execute(validar_usuario, (nombre_usuario, clave))
        registro = conexion.cursor.fetchone()

        if registro:
            print(f"\nBienvenido {registro[0]}")
            return True, registro[1]
        else:
            print("Credenciales incorrectas. Inténtalo de nuevo.")
            return False

    except mysql.connector.Error as error:
        print("Error: ", error)
        return False

    finally:
        conexion.cerrar_conexion()


def registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil):
    if clave != clave_repetida:
        return "Las claves de acceso no coinciden."

    try:
        conexion = Conexion()
        conexion.cursor.execute("USE empleados")

        conexion.cursor.execute("SELECT * FROM empleados WHERE rut = %s", (rut_empleado,))
        resultado = conexion.cursor.fetchone()
        print()

        if resultado is None:
            conexion.cerrar_conexion()
            return "El Rut ingresado no corresponde a un empleado valido."

        id_filtrado = Empleado.obtener_id(rut_empleado)

        conexion.cursor.execute(
            "SELECT * FROM perfil WHERE nombre_usuario = %s", (nombre_usuario,))
        resultado = conexion.cursor.fetchone()

        if resultado is not None:
            conexion.cerrar_conexion()
            return "El nombre de usuario ya se encuentra en uso."

        conexion.cursor.execute("INSERT INTO perfil(nombre_usuario, clave, tipo_perfil, id_empleado) VALUES(%s, %s, %s, %s)",
                                (nombre_usuario, clave, tipo_perfil, id_filtrado))
        conexion.conexion.commit()
        conexion.cerrar_conexion()

        return "El usuario se ha registrado con exito."

    except mysql.connector.Error as err:
        print(f"Algo salio mal: {err}")
        return "Ocurrio un error al intentar registrar al usuario."
