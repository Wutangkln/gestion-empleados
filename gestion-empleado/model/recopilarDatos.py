from .empleado import InformacionPersonal, InformacionLaboral, ContactoEmergencia, CargaFamiliar, Empleado
from .usuario import Usuario

from client.interfaz import menu_registro

import datetime

class RecopilarDatos:
    def recoger_informacion_personal(self):
        print("\nINFORMACION PERSONAL:")
        nombre = input("Ingresa el nombre completo: ")
        rut = input("Ingresa el RUT (12345678-9): ")
        sexo = input("Ingresa el sexo: ")
        direccion = input("Ingresa la direccion del hogar: ")
        telefono = input("Ingresa el numero de telefono: ")
        print("\n")

        return InformacionPersonal(nombre, rut, sexo, direccion, telefono)
    
    def recoger_informacion_laboral(self):
        print("INFORMACION LABORAL:")
        area = input("Ingresa el area del empleado: ")
        departamento = input("Ingresa el departamento del empleado: ")
        cargo = input("Ingresa el cargo del empleado: ")
        fecha_ingreso_str = input("Ingresa la fecha de ingreso a la empresa [YYYY-MM-DD]: ")
        fecha_ingreso = datetime.datetime.strptime(fecha_ingreso_str, '%Y-%m-%d').date()
        print("\n")

        return InformacionLaboral(cargo, area, departamento, fecha_ingreso)
    
    def recoger_contacto_emergencia(self):
        print("CONTACTO DE EMERGENCIA:")
        nombre = input("Ingresa el nombre completo: ")
        relacion = input("Ingresa la relacion con el empleado: ")
        telefono = input("Ingresa el numero de telefono: ")
        print("\n")

        return ContactoEmergencia(nombre, telefono, relacion)
    
    def recoger_carga_familiar(self):
        print("CARGAS FAMILIARES:")
        cargas = []

        while True:
            try:
                numero_cargas = int(input("Ingresa el numero de cargas familiares: "))
                break
            except ValueError:
                print("No ingresaste un numero valido. Por favor, intenta otra vez.")

        for i in range(numero_cargas):
            nombre = input("Ingresa el nombre completo: ")
            rut = input("Ingresa el RUT (12345678-9): ")
            sexo = input("Ingresa el sexo: ")
            parentesco = input("Ingresa el parentesco de la carga: ")

            carga = CargaFamiliar(nombre, rut, sexo, parentesco)
            cargas.append(carga)

        return cargas
    
    def recoger_informacion_usuario(self):
        nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil = menu_registro()
        if clave != clave_repetida:
            return "Las claves de acceso no coinciden."
        else:
            id_empleado = Empleado.obtener_id(rut_empleado)
        
            usuario = Usuario(nombre_usuario, clave, tipo_perfil)

        return usuario, id_empleado




