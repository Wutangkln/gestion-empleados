from client.interfaz import mostrar_menu_inicio, mostrar_menu_gestion ,menu_inicio_sesion, menu_registro, obtener_opcion

from model.recopilarDatos import RecopilarDatos
from model.empleado import Empleado
from model.usuario import validar_credenciales, registrar_usuario

def main():
    def agregar_empleado():
        formulario = RecopilarDatos()

        info_personal =formulario.recoger_informacion_personal()
        info_laboral = formulario.recoger_informacion_laboral()
        contacto_emergencia = formulario.recoger_contacto_emergencia()
        carga_familiar = formulario.recoger_carga_familiar()

        nuevo_empleado = Empleado(info_personal, info_laboral, contacto_emergencia, carga_familiar)
        nuevo_empleado.ingresar_informacion()
        nuevo_empleado.mostrar_informacion()

    def crear_perfil():
        formulario = RecopilarDatos()

        usuario_datos, id_empleado = formulario.recoger_informacion_usuario()
        usuario_datos.ingresar_perfil(id_empleado)

    while True:
        mostrar_menu_inicio()
        opcion = obtener_opcion()

        if opcion == "1":
            nombre_usuario, clave = menu_inicio_sesion()
            if validar_credenciales(nombre_usuario, clave):

                while True:
                    mostrar_menu_gestion()
                    opcion = obtener_opcion()

                    if opcion == "1":
                        pass

                    if opcion == "2":
                        agregar_empleado()

                    if opcion == "3":
                        pass

                    if opcion == "4":
                        pass

                    if opcion == "5":
                        crear_perfil()

                    if opcion == "6":
                        print("Se ha cerrado correctamente.")
                        break

        elif opcion == "2":
            # Guardamos en variables los valores que se registran en la interfaz "menu_registro" del fichero "client.interfaz.py"
            nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil = menu_registro()

            # Llamada a la funcion del fichero "model.usuario.py", permite el manejo de los datos almacenados
            resultado = registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil)
            print(resultado)
            # if registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil):
            #     resultado = registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil)
            #     print(resultado)
            # else:
            #     resultado = registrar_usuario(nombre_usuario, rut_empleado, clave, clave_repetida, tipo_perfil)
            #     print(resultado)

        elif opcion == "3":
            print("\nGracias por utilizar nuestro software.")
            break
        else:
            print("\nOpcion no valida. Por favor, intentalo de nuevo.")

    


        # print(f"\nUsuario: {usuario.nombre_usuario} \nTipo de perfil: {usuario.tipo_perfil} \nCreado exitosamente.")


    # app.mainloop()
    # app = Ventana()

if __name__ == '__main__':
    main()