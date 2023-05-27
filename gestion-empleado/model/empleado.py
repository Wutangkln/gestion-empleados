# Este fichero incluye toda la informacion relevante para los objetos empleados
# que luego se ingresaran a la base de datos

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