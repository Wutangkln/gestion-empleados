# Este fichero incluye toda la informacion relevante para los objetos empleados
# que luego se ingresaran a la base de datos

from .conexion import Conexion

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
            
            insertar_comando = "INSERT INTO area(nombre_area, id_departamento) VALUES(%s, %s)"
            valores_empleado = (self.info_laboral.area, self.id_departamento)
            conexion.cursor.execute(insertar_comando, valores_empleado)
            self.id_area = conexion.cursor.lastrowid
            
            insertar_comando = "INSERT INTO cargo(nombre_cargo, id_area) VALUES(%s, %s)"
            valores_empleado = (self.info_laboral.cargo, self.id_area)
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

    @staticmethod
    def obtener_id(rut):
        conexion = Conexion()
        
        try:
            conexion.cursor.execute("SELECT id_empleado FROM empleados WHERE rut = %s", (rut,))
            id_filtrado = conexion.cursor.fetchone()

            if id_filtrado is None:
                print("No fue posible encontrar al empleado con ese RUT. intenta de nuevo.")
                return None, None
            else:
                return id_filtrado[0]
            
        except Exception as error:
            print(f"Ha ocurrido un error al buscar al empleado {error}")
            return None, None

        finally:
            conexion.cerrar_conexion()