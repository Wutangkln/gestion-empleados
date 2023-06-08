import mysql.connector

class Conexion():
    def __init__(self):

        try:
            self.conexion = mysql.connector.connect(
                user="root",
                password="",
                host="localhost",
                database="gestion_empleados"
            )
            
            self.cursor = self.conexion.cursor()
        
        except mysql.connector.Error as error:
            print(f"Algo ha salido mal con la conexion, error: {error}")
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()