from .empleado import InformacionPersonal, InformacionLaboral, ContactoEmergencia, CargaFamiliar

class Formulario:
    def recoger_informacion_personal(self):
        print("INFORMACION PERSONAL:")
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
        fecha_ingreso = input("Ingresa la fecha de ingreso a la empresa: ")
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
        numero_cargas = int(input("Ingresa el numero de cargas familiares: "))

        for i in range(numero_cargas):
            nombre = input("Ingresa el nombre completo: ")
            rut = input("Ingresa el RUT (12345678-9): ")
            sexo = input("Ingresa el sexo: ")
            parentesco = input("Ingresa el parentesco de la carga: ")

            carga = CargaFamiliar(nombre, rut, sexo, parentesco)
            cargas.append(carga)

        return cargas
