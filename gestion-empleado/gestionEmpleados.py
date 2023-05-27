from client.interfaz import Ventana

from model.formulario import Formulario
from model.empleado import Empleado

def main():

    # app.mainloop()
    # app = Ventana()
    
    def agregar_empleado():
        formulario = Formulario()

        info_personal =formulario.recoger_informacion_personal()
        info_laboral = formulario.recoger_informacion_laboral()
        contacto_emergencia = formulario.recoger_contacto_emergencia()
        carga_familiar = formulario.recoger_carga_familiar()

        nuevo_empleado = Empleado(info_personal, info_laboral, contacto_emergencia, carga_familiar)
        nuevo_empleado.mostrar_informacion()

    def crear_perfil():
        formulario = Formulario()

        usuario = formulario.recoger_informacion_usuario()

        print(f"\nUsuario: {usuario.usuario} \nTipo de perfil: {usuario.tipo_perfil} \nCreado exitosamente.")

    agregar_empleado()
    crear_perfil()

if __name__ == '__main__':
    main()