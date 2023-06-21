import mysql.connector

class Conexion():
    def __init__(self):

        try:
            self.conexion = mysql.connector.connect(
                user="root",
                password="",
                host="localhost",
            )
            
            self.cursor = self.conexion.cursor()
        
        except mysql.connector.Error as error:
            print(f"Algo ha salido mal con la conexion, error: {error}")
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()

    def crear_tablas(self):
        tablas = [
            "CREATE TABLE empleados (id_empleado INT PRIMARY KEY, nombre VARCHAR(100), rut VARCHAR(20), sexo VARCHAR(20), direccion VARCHAR(100), telefono VARCHAR(20));",
            "CREATE TABLE contactos_emergencia (id_contacto_emergencia INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(100), telefono VARCHAR(20), relacion VARCHAR(100), id_empleado INT, FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));",
            "CREATE TABLE empleado_contacto (id_empleado_contacto INT PRIMARY KEY AUTO_INCREMENT, id_empleado INT, id_contacto_emergencia INT, FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado), FOREIGN KEY (id_contacto_emergencia) REFERENCES contactos_emergencia(id_contacto_emergencia));",
            "CREATE TABLE informacion_laboral (id_informacion_laboral INT PRIMARY KEY AUTO_INCREMENT, fecha_ingreso DATE, id_empleado INT, FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));",
            "CREATE TABLE departamento (id_departamento INT PRIMARY KEY AUTO_INCREMENT, nombre_departamento VARCHAR(100), id_informacion_laboral INT, FOREIGN KEY(id_informacion_laboral) REFERENCES informacion_laboral(id_informacion_laboral));",
            "CREATE TABLE area (id_area INT PRIMARY KEY AUTO_INCREMENT, nombre_area VARCHAR(100), id_departamento INT, id_empleado INT, FOREIGN KEY(id_departamento) REFERENCES departamento(id_departamento), FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));",
            "CREATE TABLE cargo (id_cargo INT PRIMARY KEY AUTO_INCREMENT, nombre_cargo VARCHAR(100), id_area INT, id_empleado INT, FOREIGN KEY(id_area) REFERENCES area(id_area), FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));",
            "CREATE TABLE cargas_familiares (id_carga_familiar INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(100), rut VARCHAR(20), sexo VARCHAR(20), parentesco VARCHAR(100), id_empleado INT, FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));",
            "CREATE TABLE perfil (id_perfil INT PRIMARY KEY AUTO_INCREMENT, nombre_usuario VARCHAR(100), clave VARCHAR(100), tipo_perfil VARCHAR(100), id_empleado INT, FOREIGN KEY (id_empleado) REFERENCES empleados(id_empleado));"
        ]

        try:
            self.cursor.execute("SHOW DATABASES LIKE 'empleados'")
            resultado = self.cursor.fetchone()

            if resultado:
                print("La base de datos ya se encuentra creada.")
            else:
                self.cursor.execute("CREATE DATABASE IF NOT EXISTS empleados;")
                self.cursor.execute("USE empleados;")
                
                for tabla in tablas:
                    try:
                        self.cursor.execute(tabla)
                        print(f"Tabla creada: {tabla}")
                    except Exception as e:
                        print(f"No se pudo crear la tabla: {tabla}")
                        print(f"Error: {e}")
                        
        except Exception as e:
            print(f"No se pudo crear la base de datos. Error: {e}")
            
        


