import mysql.connector

class Conexion():
    def __init__(self, user, password, host, database):

        try:
            conexion = mysql.connector.connect(
                user=user,
                password=password,
                host=host,
                database=database
            )
            print("Conexion establecida con la base de datos:", database)
        
        except mysql.connector.Error as err:
            print(f"Algo ha salido mal con la conexion, error: {err}")

        finally:
            conexion.close()
            print("conexion cerrarda")

    def creacion_tablas(self):
        pass


# db = Conexion("root", "", "localhost", "gestion_empleados")
    