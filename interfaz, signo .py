import tkinter as tk
from tkinter import messagebox

class SignoZodiacal:
    def __init__(self, nombre, dia, mes):
        self.nombre = nombre
        self.dia = dia
        self.mes = mes

    def obtener_signo_zodiacal(self):
        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Géminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cáncer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Fecha inválida"

    def mostrar_informacion(self):
        signo_zodiacal = self.obtener_signo_zodiacal()
        return f"{self.nombre}, nacido el {self.dia}/{self.mes}, pertenece al signo zodiacal: {signo_zodiacal}."

def calcular_signo():
    nombre = entry_nombre.get()
    dia = entry_dia.get()
    mes = entry_mes.get()

    try:
        dia = int(dia)
        mes = int(mes)

        if not (1 <= dia <= 31 and 1 <= mes <= 12):
            raise ValueError

        signo = SignoZodiacal(nombre, dia, mes)
        resultado = signo.mostrar_informacion()
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un día y mes válidos.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")
ventana.geometry("300x200")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_dia = tk.Label(ventana, text="Día de nacimiento:")
label_dia.pack()
entry_dia = tk.Entry(ventana)
entry_dia.pack()

label_mes = tk.Label(ventana, text="Mes de nacimiento:")
label_mes.pack()
entry_mes = tk.Entry(ventana)
entry_mes.pack()

# Botón para calcular el signo zodiacal
boton_calcular = tk.Button(ventana, text="Calcular Signo", command=calcular_signo)
boton_calcular.pack()

# Ejecutar la ventana principal
ventana.mainloop()
