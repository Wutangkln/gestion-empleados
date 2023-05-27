from client.interfaz import Ventana
from model.formulario import Formulario
from model.empleado import Empleado



def main():
    
    def agregar_empleado():
        formulario = Formulario()

        info_personal =formulario.recoger_informacion_personal()
        info_laboral = formulario.recoger_informacion_laboral()
        contacto_emergencia = formulario.recoger_contacto_emergencia()
        carga_familiar = formulario.recoger_carga_familiar()

        nuevo_empleado = Empleado(info_personal, info_laboral, contacto_emergencia, carga_familiar)
        nuevo_empleado.mostrar_informacion()

    agregar_empleado()

    # app = Ventana()
    # app.mainloop()
    
if __name__ == '__main__':
    main()