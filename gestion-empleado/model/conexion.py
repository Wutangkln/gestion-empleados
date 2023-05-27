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
        
        except mysql.connector.Error as error:
            print(f"Algo ha salido mal con la conexion, error: {error}")

        finally:
            conexion.close()
            print("La conexion con la base de datos ha sido cerrada correctamente.")

    def creacion_tablas(self):
        pass


# db = Conexion("root", "", "localhost", "gestion_empleados")
    