# Este fichero incluye toda la informacion relevante para los objetos empleados
# que luego se ingresaran a la base de datos

from .conexion import Conexion
import mysql

class InformacionPersonal():
    def __init__(self, nombre, rut, sexo, direccion, telefono):
        self.nombre = nombre
        self.rut = rut
        self.sexo = sexo
        self.direccion = direccion
        self.telefono = telefono

class InformacionLaboral:
    def __init__(self, cargo, area, departamento, fecha_ingreso):
        self.cargo = cargo
        self.area = area
        self.departamento = departamento
        self.fecha_ingreso = fecha_ingreso

class ContactoEmergencia:
    def __init__(self, nombre, telefono, relacion):
        self.nombre = nombre
        self.telefono = telefono
        self.relacion = relacion

class CargaFamiliar:
    def __init__(self, nombre, rut, sexo, parentesco):
        self.nombre = nombre
        self.rut = rut
        self.sexo = sexo
        self.parentesco = parentesco

class Empleado:
    def __init__(self, info_personal, info_laboral, contacto_emergencia, cargas_familiares):
        self.info_personal = info_personal
        self.info_laboral = info_laboral
        self.contacto_emergencia = contacto_emergencia
        self.cargas_familiares = cargas_familiares

    def mostrar_informacion(self):
        print(f'''
    INFORMACION PERSONAL: \n 
        Nombre: {self.info_personal.nombre}
        RUT: {self.info_personal.rut}
        Sexo: {self.info_personal.sexo}
        Telefono: {self.info_personal.telefono}
        Direccion: {self.info_personal.direccion} \n

    INFORMACION LABORAL: \n 
        Fecha de ingreso: {self.info_laboral.fecha_ingreso}
        Departamento: {self.info_laboral.departamento}
        Area: {self.info_laboral.area}
        Cargo: {self.info_laboral.cargo}

    CONTACTO DE EMERGENCIA: \n 
        Nombre: {self.contacto_emergencia.nombre}
        Telefono: {self.contacto_emergencia.telefono}
        Relacion: {self.contacto_emergencia.relacion} \n
         ''')
        
        for carga in self.cargas_familiares:
            print(f'''
    CARGAS FAMILIARES: \n
        Nombre: {carga.nombre}
        RUT: {carga.rut}
        Sexo: {carga.sexo}
        Parentesco: {carga.parentesco} \n
            ''')
            
    def ingresar_informacion(self):
        print("ENTRO AL METODO INGRESAR_INFORMACION")
        try:
            conexion = Conexion()
            conexion.cursor.execute("USE empleados")

            # insersion de datos a la tabla empleado
            insertar_comando = "INSERT INTO empleados(nombre, rut, sexo, direccion, telefono) VALUES(%s, %s, %s, %s, %s)"
            valores_empleado = (self.info_personal.nombre, self.info_personal.rut, self.info_personal.sexo, self.info_personal.direccion, self.info_personal.telefono)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_empleado = conexion.cursor.lastrowid  # lastrowid obtiene el id, entonces lo guardamos en una variable

            # insersion de datos a la tabla informacion laboral
            insertar_comando = "INSERT INTO informacion_laboral(fecha_ingreso, id_empleado) VALUES(%s, %s)"
            valores_empleado = (self.info_laboral.fecha_ingreso, self.id_empleado)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_laboral = conexion.cursor.lastrowid

            insertar_comando = "INSERT INTO departamento(nombre_departamento, id_informacion_laboral) VALUES(%s, %s)"
            valores_empleado = (self.info_laboral.departamento, self.id_laboral)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_departamento = conexion.cursor.lastrowid
            
            insertar_comando = "INSERT INTO area(nombre_area, id_departamento, id_empleado) VALUES(%s, %s, %s)"
            valores_empleado = (self.info_laboral.area, self.id_departamento, self.id_empleado)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_area = conexion.cursor.lastrowid
            
            insertar_comando = "INSERT INTO cargo(nombre_cargo, id_area, id_empleado) VALUES(%s, %s, %s)"
            valores_empleado = (self.info_laboral.cargo, self.id_area, self.id_empleado)
            conexion.cursor.execute(insertar_comando, valores_empleado)

            # insersion de datos a la tabla contacto de emergencia
            insertar_comando = "INSERT INTO contactos_emergencia(nombre, telefono, relacion, id_empleado) VALUES(%s, %s, %s, %s)"
            valores_empleado = (self.contacto_emergencia.nombre, self.contacto_emergencia.telefono, self.contacto_emergencia.relacion, self.id_empleado)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_contacto_emergencia = conexion.cursor.lastrowid

            # insersion de datos a la tabla empleado_contacto
            insertar_comando = "INSERT INTO empleado_contacto(id_empleado, id_contacto_emergencia) VALUES(%s, %s)"
            valores_empleado = (self.id_empleado, self.id_contacto_emergencia)
            conexion.cursor.execute(insertar_comando, valores_empleado)

            for carga in self.cargas_familiares:
                insertar_comando = "INSERT INTO cargas_familiares(nombre, rut, sexo, parentesco, id_empleado) VALUES(%s, %s, %s, %s, %s)"
                valores_empleado = (carga.nombre, carga.rut, carga.sexo, carga.parentesco, self.id_empleado)
                conexion.cursor.execute(insertar_comando, valores_empleado)

            conexion.conexion.commit()
            
            print(f"Se ha ingresado correctamente los datos registrados del empleado: {self.info_personal.nombre}")

        except Exception as error:
            conexion.conexion.rollback()
            print(f"Se produjo un error: {error}")
        
        finally:
            conexion.cerrar_conexion()

    def mostrar_lista_empleados():
        try:
            conexion = Conexion()
            conexion.cursor.execute("USE empleados")
            mostrar_comando = """
            SELECT e.nombre, e.rut, e.sexo, c.nombre_cargo
            FROM empleados e
            INNER JOIN informacion_laboral il ON e.id_empleado = il.id_empleado
            INNER JOIN departamento d ON il.id_informacion_laboral = d.id_informacion_laboral
            INNER JOIN area a ON d.id_departamento = a.id_departamento
            INNER JOIN cargo c ON a.id_area = c.id_area
            """
            conexion.cursor.execute(mostrar_comando)
            empleados = conexion.cursor.fetchall()

            if empleados:
                print("--- Lista de Empleados ---")
                for empleado in empleados:
                    print(f"Nombre: {empleado[0]} | RUT: {empleado[1]} | Sexo: {empleado[2]} | Cargo: {empleado[3]}")
                print("----------------------------")
            else:
                print("No hay empleados registrados en el sistema, por favor reintente más tarde.")

            conexion.cerrar_conexion()

        except mysql.connector.Error as err:
            print(f"Algo salió mal: {err}")
  
    def actualizar_informacion_personal(self, id_filtrado):
        try:
            conexion = Conexion()
            conexion.cursor.execute("USE empleados")

            actualizar_comando = '''
            UPDATE empleados
            SET nombre = %s, rut = %s, sexo = %s, direccion = %s, telefono = %s   
            WHERE id_empleado = %s   
            '''
            datos = (self.info_personal.nombre, self.info_personal.rut, self.info_personal.sexo, self.info_personal.direccion, self.info_personal.telefono, id_filtrado)

            conexion.cursor.execute(actualizar_comando, datos)
            conexion.conexion.commit()

            print("La informacion personal del empleado ha sido actualizada con exito.")

        except mysql.connector.Error as error:
            conexion.conexion.rollback()
            print(f"Ha ocurrido un error al intentar actualizar la informacion personal: {error}")

        finally:
            conexion.cerrar_conexion()      

    @staticmethod
    def obtener_id(rut):
        conexion = Conexion()
        
        try:
            conexion.cursor.execute("USE empleados")
            conexion.cursor.execute("SELECT id_empleado FROM empleados WHERE rut = %s", (rut,))
            id_filtrado = conexion.cursor.fetchone()

            if id_filtrado is None:
                print("No fue posible encontrar al empleado con ese RUT. intenta de nuevo.")
                return None, None
            else:
                print("Empleado encontrado con exito.")
                return id_filtrado[0], None
            
        except Exception as error:
            print(f"Ha ocurrido un error al buscar al empleado {error}")
            return None, None

        finally:
            conexion.cerrar_conexion()

    def obtener_empleado(id_empleado):
        conexion = Conexion()
        
        try:
            conexion.cursor.execute("USE empleados")
            conexion.cursor.execute("SELECT * FROM empleados WHERE id_empleado = %s", (id_empleado,))
            empleado_data = conexion.cursor.fetchone()

            print("DATOS TABLA EMPLEADOS: ", empleado_data)

            if empleado_data is None:
                print("No fue posible encontrar al empleado con ese ID. Inténtalo de nuevo.")
                return None

            # Obtener la información personal del empleado
            info_personal = InformacionPersonal(empleado_data[1], empleado_data[2], empleado_data[3], empleado_data[4], empleado_data[5])

            # Obtener la información laboral del empleado
            conexion.cursor.execute("SELECT * FROM informacion_laboral WHERE id_empleado = %s", (id_empleado,))
            info_laboral_data = conexion.cursor.fetchone()

            conexion.cursor.execute("SELECT * FROM departamento WHERE id_informacion_laboral = %s", (info_laboral_data[0],))
            departamento_data = conexion.cursor.fetchone()

            conexion.cursor.execute("SELECT * FROM area WHERE id_departamento = %s", (departamento_data[0],))
            area_data = conexion.cursor.fetchone()

            conexion.cursor.execute("SELECT * FROM cargo WHERE id_area = %s", (area_data[0],))
            cargo_data = conexion.cursor.fetchone()

            print("DATOS TABLA INFORMACION LABORAL", info_laboral_data)
            print("DATOS TABLA DEPARTAMENTO", departamento_data)
            print("DATOS TABLA AREA", area_data)
            print("DATOS TABLA CARGO", cargo_data)

            info_laboral = InformacionLaboral(info_laboral_data[1], departamento_data[1], area_data[1], cargo_data[1])

            # Obtener el contacto de emergencia del empleado
            conexion.cursor.execute("SELECT * FROM contactos_emergencia WHERE id_empleado = %s", (id_empleado,))
            contacto_emergencia_data = conexion.cursor.fetchone()
            contacto_emergencia = ContactoEmergencia(contacto_emergencia_data[1], contacto_emergencia_data[2], contacto_emergencia_data[3])

            # Obtener las cargas familiares del empleado
            conexion.cursor.execute("SELECT * FROM cargas_familiares WHERE id_empleado = %s", (id_empleado,))
            cargas_familiares_data = conexion.cursor.fetchall()
            cargas_familiares = []
            for carga_data in cargas_familiares_data:
                carga_familiar = CargaFamiliar(carga_data[1], carga_data[2], carga_data[3], carga_data[4])
                cargas_familiares.append(carga_familiar)

            empleado = Empleado(info_personal, info_laboral, contacto_emergencia, cargas_familiares)
            return empleado

        except Exception as error:
            print(f"Ha ocurrido un error al obtener los datos del empleado: {error}")
            return None

        finally:
            conexion.cerrar_conexion()