from client.interfaz import mostrar_menu_inicio, mostrar_menu_gestion ,menu_inicio_sesion, menu_registro, obtener_opcion

from model.formulario import Formulario
from model.empleado import Empleado
from model.usuario import validar_credenciales, registrar_usuario

def main():

    while True:
        mostrar_menu_inicio()
        opcion = obtener_opcion()

        if opcion == "1":
            nombre_usuario, clave = menu_inicio_sesion()
            if validar_credenciales(nombre_usuario, clave):
                mostrar_menu_gestion()
                opcion = obtener_opcion()

        elif opcion == "2":
            # Guardamos en variables los valores que se registran en la interfaz "menu_registro" del fichero "client.interfaz.py"
            nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil = menu_registro()

            if tipo_perfil.lower() in ["administrador", "normal"]:
                1
                # Llamada a la funcion del fichero "model.usuario.py", permite el manejo de los datos almacenados
                if registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil):
                    resultado = registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil)
                    print(resultado)
                else:
                    resultado = registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil)
                    print(resultado)

            else:
                print("lo siento, ingresa un valor correcto en el campo 'seleccion de perfil'. Intentalo otra vez.")

        elif opcion == "3":
            print("\nGracias por utilizar nuestro software.")
            break
        else:
            print("\nOpcion no valida. Por favor, intentalo de nuevo.")

    
    # def agregar_empleado():
    #     formulario = Formulario()

    #     info_personal =formulario.recoger_informacion_personal()
    #     info_laboral = formulario.recoger_informacion_laboral()
    #     contacto_emergencia = formulario.recoger_contacto_emergencia()
    #     carga_familiar = formulario.recoger_carga_familiar()

    #     nuevo_empleado = Empleado(info_personal, info_laboral, contacto_emergencia, carga_familiar)
    #     nuevo_empleado.mostrar_informacion()

    # def crear_perfil():
    #     formulario = Formulario()

    #     usuario = formulario.recoger_informacion_usuario()

    #     print(f"\nUsuario: {usuario.usuario} \nTipo de perfil: {usuario.tipo_perfil} \nCreado exitosamente.")

    # agregar_empleado()
    # crear_perfil()

    # app.mainloop()
    # app = Ventana()

if __name__ == '__main__':
    main()