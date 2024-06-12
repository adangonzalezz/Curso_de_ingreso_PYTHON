import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import math

'''
nombre: Adan Yael 
apellido: Gonzalez Arias
---
De los 50 participantes del torneo de UTN-TETRIS, se debe ingresar los siguientes datos:

Nombre
Categoría (Principiante - Intermedio - Avanzado)
Edad (entre 18 y 99 inclusive)
Score (mayor que 0)
Nivel alcanzado (1 , 2 o 3)

Pedir datos por prompt y mostrar por print, se debe informar:

    Informe A- Cuál es la categoría que tiene más participantes.
    Informe B- El Porcentaje de jugadores de la categoría avanzado sobre el total
    Informe C- La categoría del participante de menor Score
    Informe D- El score y nombre del avanzado con mayor edad
    Informe E- Promedio de score de los participantes principiantes.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        seguir = True

        contador_pr = 0
        contador_int = 0
        contador_av = 0

        score_min = 0
        bandera_min = False
        categoria_min = ""

        edad_av = 0
        score_av = 0
        nombre_av = ""
        bandera_av = False

        score_pr = 0
        promedio_score_pr = 0


        while seguir == True:
            nombre = prompt("", "Ingrese su nombre")

            categoria = prompt("", "Ingrese su categoria")
            while categoria != "Principiante" and categoria != "Intermedio" and categoria != "Avanzado":
                categoria = prompt("", "Reingrese su categoria")

            edad = int(prompt("", "Ingrese su edad"))
            while edad < 18 or edad > 99:
                edad = int(prompt("", "Reingrese su edad"))

            score = int(prompt("", "Ingrese su score"))
            while score <= 0:
                score = int(prompt("", "Reingrese su score"))

            Nivel = int(prompt("", "Ingrese su Nivel"))
            while Nivel != 1 and Nivel != 2 and Nivel != 3:
                Nivel = int(prompt("", "Reingrese su Nivel"))

            match categoria:
                case "Principiante":
                    contador_pr += 1
                    score_pr += score
                case "Intermedio":
                    contador_int += 1
                case _:
                    contador_av += 1

            if score < score_min or bandera_min == False:
                score_min = score
                categoria_min = categoria
                bandera_min = True

            if categoria == "Avanzado" and (edad > edad_av or bandera_av == False):
                nombre_av = nombre
                score_av = score
                edad_av = edad
                bandera_av = True



            seguir = question("", "Desea ingresar otro participante?")

        if contador_pr > contador_int and contador_pr > contador_av:
            mas_participantes = "La categoria con mas participantes es la Principiante"
        elif contador_int > contador_pr and contador_int > contador_av:
            mas_participantes = "La categoria con mas participantes es la Intermedia"
        else:
            mas_participantes = "La categoria con mas participantes es la Avanzada"

        total_participantes = contador_pr + contador_int + contador_av
        promedio_av = (contador_av * 100) / total_participantes

        if categoria == "Principiante":
            promedio_score_pr = (score_pr / contador_pr)
            if promedio_score_pr == 0:
                promedio_score_pr = score_pr


        print("A. {}".format(mas_participantes))
        print("B. El porcentaje de participantes avanzados es de {0}".format(promedio_av))
        print("C. La categoría del participante de menor Score es {0}".format(categoria_min))
        print("D. El participante Avanzado con mas edad tiene un Score de {0} y se llama {1}".format(score_av, nombre_av))
        print("E. El Score promedio de los participantes principiantes es de {0}".format(promedio_score_pr))





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()