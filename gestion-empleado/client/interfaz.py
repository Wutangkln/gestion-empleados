import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageFilter, ImageTk

# from tkinter import *
# from tkinter import messagebox


class Ventana(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Acceso al sistema")
        self.geometry("300x450")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.marco_sesion = Marco_sesion(self)
        self.marco_sesion.grid(row=0, column=0, pady=20, padx=30, sticky='nsew')
        # configuramos la grilla del marco a 4 filas y 1 columna
        self.marco_sesion.grid_rowconfigure(5, weight=1)
        self.marco_sesion.grid_columnconfigure(0, weight=1)

class Marco_sesion(ctk.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.botones_sesion()

    def botones_sesion(self):
        self.etiqueta_imagen = ctk.CTkLabel(
            self, 
            text="IMAGEN",
            text_color=("gray70"),
            font=ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_imagen.grid(row=0, column=0, pady=30, padx=10)

        self.etiqueta_titulo = ctk.CTkLabel(
            self, 
            text="Acceso al sistema",
            fg_color=("gray50"), 
            text_color=("gray70"), 
            font=ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_titulo.grid(row=1, column=0, pady=30, sticky="ew")

        self.boton_inicio = ctk.CTkButton(
            self, 
            text="Iniciar Sesion",
            height=40,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"),
            command=self.abrir_marco_inicio)
        self.boton_inicio.grid(row=2, column=0, padx=15, pady=(30, 10), sticky="ew")

        self.boton_registrase = ctk.CTkButton(
            self, 
            text="Registrarse",
            height=40,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"),
            command=self.abrir_marco_registrarse)
        self.boton_registrase.grid(row=3, column=0, padx=15, pady=10, sticky="ew")
        
        self.boton_registrase = ctk.CTkButton(
            self, 
            text="Salir",
            height=15,
            width=25,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"),
            command=lambda : self.quit())
        self.boton_registrase.grid(row=5, column=0, padx=15, pady=(30, 10))

    def abrir_marco_inicio(self):
        self.marco_inicio = ctk.CTkToplevel()
        self.marco_inicio.title("Inicio de sesion")
        self.marco_inicio.geometry("300x450")
        self.marco_inicio.attributes("-topmost", True)
        self.marco_inicio.grab_set()
        self.marco_inicio.grid_rowconfigure(0, weight=1)
        self.marco_inicio.grid_columnconfigure(0, weight=1)

        self.sub_marco_inicio = ctk.CTkFrame(self.marco_inicio)
        self.sub_marco_inicio.grid(row=0, column=0, pady=20, padx=30, sticky="nsew")
        self.sub_marco_inicio.grid_rowconfigure(7, weight=1)
        self.sub_marco_inicio.grid_columnconfigure(0, weight=1)

        self.etiqueta_titulo_inicio = ctk.CTkLabel(
            self.sub_marco_inicio, 
            text="Inicio de sesion",
            fg_color=("gray50"), 
            text_color=("gray70"), 
            font=ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_titulo_inicio.grid(row=0, column=0, pady=20, sticky="ew")

        self.inicio_usuario = ctk.CTkLabel(
            self.sub_marco_inicio, 
            text="Nombre de usuario",
            text_color=("gray70"), 
            font=ctk.CTkFont(size=12))
        self.inicio_usuario.grid(row=1, column=0, pady=(20, 10), sticky="ew")
        self.input_inicio_usuario = ctk.CTkEntry(self.sub_marco_inicio)
        self.input_inicio_usuario.grid(row=2, column=0, pady=(0, 10), padx=10)

        self.inicio_clave = ctk.CTkLabel(
            self.sub_marco_inicio, 
            text="Clave de acceso",
            text_color=("gray70"), 
            font=ctk.CTkFont(size=12))
        self.inicio_clave.grid(row=3, column=0, pady=(10, 0), sticky="ew")
        self.input_inicio_clave = ctk.CTkEntry(self.sub_marco_inicio)
        self.input_inicio_clave.grid(row=4, column=0, pady=(10, 30), padx=10)

        self.sub_marco_boton_iniciar = ctk.CTkButton(
            self.sub_marco_inicio, 
            text="Iniciar sesion",
            height=40,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"))
        self.sub_marco_boton_iniciar.grid(row=5, column=0, padx=15, pady=10, sticky="ew")

        self.sub_marco_boton_salir = ctk.CTkButton(
            self.sub_marco_inicio, 
            text="Salir",
            height=15,
            width=25,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"),
            command=lambda : self.marco_inicio.destroy())
        self.sub_marco_boton_salir.grid(row=6, column=0, padx=15, pady=10)


    def abrir_marco_registrarse(self):
        self.marco_registrarse = ctk.CTkToplevel()
        self.marco_registrarse.title("Registrarse")
        self.marco_registrarse.geometry("300x550")
        self.marco_registrarse.attributes("-topmost", True)
        self.marco_registrarse.grab_set()
        self.marco_registrarse.grid_rowconfigure(0, weight=1)
        self.marco_registrarse.grid_columnconfigure(0, weight=1)

        self.sub_marco_registrarse = ctk.CTkFrame(self.marco_registrarse)
        self.sub_marco_registrarse.grid(row=0, column=0, pady=20, padx=30, sticky="nsew")
        self.sub_marco_registrarse.grid_rowconfigure(9, weight=1)
        self.sub_marco_registrarse.grid_columnconfigure(0, weight=1)

        self.etiqueta_titulo_registrarse = ctk.CTkLabel(
            self.sub_marco_registrarse, 
            text="Registrarse",
            fg_color=("gray50"), 
            text_color=("gray70"), 
            font=ctk.CTkFont(size=18, weight="bold"))
        self.etiqueta_titulo_registrarse.grid(row=0, column=0, pady=20, sticky="ew")
    
        self.registro_usuario = ctk.CTkLabel(
            self.sub_marco_registrarse, 
            text="Nombre de usuario",
            text_color=("gray70"), 
            font=ctk.CTkFont(size=12))
        self.registro_usuario.grid(row=1, column=0, pady=(20, 10), sticky="ew")
        self.input_registro_usuario = ctk.CTkEntry(self.sub_marco_registrarse)
        self.input_registro_usuario.grid(row=2, column=0, pady=(0, 10), padx=10)

        self.etiqueta_registro_clave = ctk.CTkLabel(
            self.sub_marco_registrarse, 
            text="Clave de acceso",
            text_color=("gray70"), 
            font=ctk.CTkFont(size=12))
        self.etiqueta_registro_clave.grid(row=3, column=0, pady=(10, 0), sticky="ew")
        self.input_registro_clave = ctk.CTkEntry(self.sub_marco_registrarse)
        self.input_registro_clave.grid(row=4, column=0, pady=(10, 10), padx=10)

        self.valores = ["Administrador","Normal"]

        self.etiqueta_registro_perfil = ctk.CTkLabel(
            self.sub_marco_registrarse, 
            text="Tipo de perfil",
            text_color=("gray70"), 
            font=ctk.CTkFont(size=12))
        self.etiqueta_registro_perfil.grid(row=5, column=0, pady=(10, 0), sticky="ew")
        self.input_registro_perfil = ctk.CTkOptionMenu(
            self.sub_marco_registrarse, 
            values=self.valores,
            fg_color="gray40",
            text_color="gray20",
            button_hover_color="gray60",
            dropdown_hover_color="gray60",
            button_color="gray40")
        self.input_registro_perfil.grid(row=6, column=0, pady=(10, 30), padx=10)

        self.sub_marco_boton_registrarse = ctk.CTkButton(
            self.sub_marco_registrarse, 
            text="Registrate",
            height=40,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"))
        self.sub_marco_boton_registrarse.grid(row=7, column=0, padx=15, pady=10, sticky="ew")

        self.sub_marco_boton_salir = ctk.CTkButton(
            self.sub_marco_registrarse, 
            text="Salir",
            height=15,
            width=25,
            border_spacing=10,
            fg_color="gray40",
            text_color=("gray20"),
            hover_color=("gray60"),
            command=lambda : self.marco_registrarse.destroy())
        self.sub_marco_boton_salir.grid(row=8, column=0, padx=15, pady=10)


 
 
# class Pycalc(Frame):
 
#     def __init__(self, master, *args, **kwargs):
#         Frame.__init__(self, master, *args, **kwargs)
#         self.parent = master
#         self.grid()
#         self.createWidgets()
 
#     def deleteLastCharacter(self):
#         textLength = len(self.display.get())
 
#         if textLength >= 1:
#             self.display.delete(textLength - 1, END)
#         if textLength == 1:
#             self.replaceText("0")
 
#     def replaceText(self, text):
#         self.display.delete(0, END)
#         self.display.insert(0, text)
 
#     def append(self, text):
#         actualText = self.display.get()
#         textLength = len(actualText)
#         if actualText == "0":
#             self.replaceText(text)
#         else:
#             self.display.insert(textLength, text)
 
#     def evaluate(self):
#         try:
#             self.replaceText(eval(self.display.get()))
#         except (SyntaxError, AttributeError):
#             messagebox.showerror("Error", "Syntax Error")
#             self.replaceText("0")
#         except ZeroDivisionError:
#             messagebox.showerror("Error", "Cannot Divide by 0")
#             self.replaceText("0")
 
#     def containsSigns(self):
#         operatorList = ["*", "/", "+", "-"]
#         display = self.display.get()
#         for c in display:
#             if c in operatorList:
#                  return True
#         return False
 
#     def changeSign(self):
#         if self.containsSigns():
#             self.evaluate()
#         firstChar = self.display.get()[0]
#         if firstChar == "0":
#             pass
#         elif firstChar == "-":
#             self.display.delete(0)
#         else:
#             self.display.insert(0, "-")
 
#     def inverse(self):
#         self.display.insert(0, "1/(")
#         self.append(")")
#         self.evaluate()
 
#     def createWidgets(self):
#         self.display = Entry(self, font=("Arial", 24), relief=RAISED, justify=RIGHT, bg='darkblue', fg='red', borderwidth=0)
#         self.display.insert(0, "0")
#         self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")
 
#         self.ceButton = Button(self, font=("Arial", 12), fg='red', text="CE", highlightbackground='red', command=lambda: self.replaceText("0"))
#         self.ceButton.grid(row=1, column=0, sticky="nsew")
#         self.inverseButton = Button(self, font=("Arial", 12), fg='red', text="1/x", highlightbackground='lightgrey', command=lambda: self.inverse())
#         self.inverseButton.grid(row=1, column=2, sticky="nsew")
#         self.delButton = Button(self, font=("Arial", 12), fg='#e8e8e8', text="Del", highlightbackground='red', command=lambda: self.deleteLastCharacter())
#         self.delButton.grid(row=1, column=1, sticky="nsew")
#         self.divButton = Button(self, font=("Arial", 12), fg='red', text="/", highlightbackground='lightgrey', command=lambda: self.append("/"))
#         self.divButton.grid(row=1, column=3, sticky="nsew")
 
#         self.sevenButton = Button(self, font=("Arial", 12), fg='white', text="7", highlightbackground='black', command=lambda: self.append("7"))
#         self.sevenButton.grid(row=2, column=0, sticky="nsew")
#         self.eightButton = Button(self, font=("Arial", 12), fg='white', text="8", highlightbackground='black', command=lambda: self.append("8"))
#         self.eightButton.grid(row=2, column=1, sticky="nsew")
#         self.nineButton = Button(self, font=("Arial", 12), fg='white', text="9", highlightbackground='black', command=lambda: self.append("9"))
#         self.nineButton.grid(row=2, column=2, sticky="nsew")
#         self.multButton = Button(self, font=("Arial", 12), fg='red', text="*", highlightbackground='lightgrey', command=lambda: self.append("*"))
#         self.multButton.grid(row=2, column=3, sticky="nsew")
 
#         self.fourButton = Button(self, font=("Arial", 12), fg='white', text="4", highlightbackground='black', command=lambda: self.append("4"))
#         self.fourButton.grid(row=3, column=0, sticky="nsew")
#         self.fiveButton = Button(self, font=("Arial", 12), fg='white', text="5", highlightbackground='black', command=lambda: self.append("5"))
#         self.fiveButton.grid(row=3, column=1, sticky="nsew")
#         self.sixButton = Button(self, font=("Arial", 12), fg='white', text="6", highlightbackground='black', command=lambda: self.append("6"))
#         self.sixButton.grid(row=3, column=2, sticky="nsew")
#         self.minusButton = Button(self, font=("Arial", 12), fg='red', text="-", highlightbackground='lightgrey', command=lambda: self.append("-"))
#         self.minusButton.grid(row=3, column=3, sticky="nsew")
 
#         self.oneButton = Button(self, font=("Arial", 12), fg='white', text="1", highlightbackground='black', command=lambda: self.append("1"))
#         self.oneButton.grid(row=4, column=0, sticky="nsew")
#         self.twoButton = Button(self, font=("Arial", 12), fg='white', text="2", highlightbackground='black', command=lambda: self.append("2"))
#         self.twoButton.grid(row=4, column=1, sticky="nsew")
#         self.threeButton = Button(self, font=("Arial", 12), fg='white', text="3", highlightbackground='black', command=lambda: self.append("3"))
#         self.threeButton.grid(row=4, column=2, sticky="nsew")
#         self.plusButton = Button(self, font=("Arial", 12), fg='red', text="+", highlightbackground='lightgrey', command=lambda: self.append("+"))
#         self.plusButton.grid(row=4, column=3, sticky="nsew")
 
#         self.negToggleButton = Button(self, font=("Arial", 12), fg='red', text="+/-", highlightbackground='lightgrey', command=lambda: self.changeSign())
#         self.negToggleButton.grid(row=5, column=0, sticky="nsew")
#         self.zeroButton = Button(self, font=("Arial", 12), fg='white', text="0", highlightbackground='black', command=lambda: self.append("0"))
#         self.zeroButton.grid(row=5, column=1, sticky="nsew")
#         self.decimalButton = Button(self, font=("Arial", 12), fg='white', text=".", highlightbackground='lightgrey', command=lambda: self.append("."))
#         self.decimalButton.grid(row=5, column=2, sticky="nsew")
#         self.equalsButton = Button(self, font=("Arial", 12), fg='red', text="=", highlightbackground='lightgrey', command=lambda: self.evaluate())
#         self.equalsButton.grid(row=5, column=3, sticky="nsew")
 
 
# Calculator = Tk()
# Calculator.title("AdictoCalculator")
# Calculator.resizable(False, False)
# Calculator.config(cursor="pencil")
# root = Pycalc(Calculator).grid()
# Calculator.mainloop()