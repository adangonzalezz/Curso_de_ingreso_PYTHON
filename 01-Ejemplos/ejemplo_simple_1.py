import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Adan Yael
apellido: Gonzalez Arias
---

Nombre

Edad (debe ser mayor a 12)

Altura (no debe ser negativa)

Días que asiste a la semana (1, 3, 5)

Kilos que levanta en peso muerto (no debe ser cero, ni negativo)



No sabemos cuántos clientes serán consultados.

Se debe informar al usuario:

1 El promedio de kilos que levantan las personas que asisten solo 3 días a la semana.

2 El porcentaje de clientes que asiste solo 1 día a la semana.

3 Nombre y edad del cliente con más altura.

4 Determinar si los clientes eligen más ir 1, 3 o 5 días

5 Nombre y cantidad de kilos levantados en peso muerto, de la persona más joven que solo asista 5 días a la semana.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        seguir = True

        nombre = ""
        altura = 0
        edad = 0
        dias = 0
        kilos = 0

        contador_1 = 0
        contador_3 = 0
        contador_5 = 0

        acumulador_k_d = 0

        altura_max = 0
        nombre_max = ""
        edad_max = 0
        bandera_alt_max = False

        nombre_min = ""
        edad_min = 0
        kilos_min = 0
        bandera_edad_min = False

        promedio = 0



        while seguir :
            nombre = input("Ingrese su nombre ")

            edad = int(input("ingrese su edad"))
            while edad < 12:
                edad = int(input("reingrese su edad"))

            altura = int(input("ingrese su altura"))
            while altura <= 0:
                altura = int(input("reingrese su altura"))

            dias = int(input("Ingrese la cantidad de dias"))
            while dias != 1 and dias != 3 and dias != 5:
                dias =int(input("Reingrese la cantidad de dias"))

            kilos = int(input("Ingrese la cantidad de kilos levantados"))
            while kilos <= 0:
                kilos = int(input("Reingrese la cantidad de kilos levantados"))

            if altura > altura_max or bandera_alt_max == False:
                altura_max = altura
                nombre_max = nombre
                edad_max = edad
                bandera_alt_max = True

            if edad < edad_min or bandera_edad_min == False:
                nombre_min = nombre
                edad_min = edad
                kilos_min = kilos
                bandera_edad_min = True
                # datos que se repiten

            match dias:
                case 1:
                    contador_1 += 1
                case 3:
                    contador_3 += 1
                    acumulador_k_d += kilos
                case 5:
                    contador_5 += 1

                    
            
            

            seguir = question("Seguir", "Ingresa otro cliente?")

        if dias == 3:
            promedio = acumulador_k_d / contador_3

        if contador_1 > contador_3 and  contador_1 > contador_5:
            cant_dias_mas_c = "Los clientes elijen mas ir 1 dias"
        elif contador_3 > contador_1 and contador_3 >contador_5:
            cant_dias_mas_c = "Los clientes elijen mas ir 3 dias"
        else:
            cant_dias_mas_c = "Los clientes elijen mas ir 5 dias"


        
        total_clientes = contador_1 + contador_3 + contador_1
        promedio_dia_1 = (contador_1 * 100) / total_clientes




        print("1. El promedio de peso levantado es de {0}".format(promedio))
        print("2. El promedio de asistentes del dia 1 es del {0}".format(promedio_dia_1))
        print("3. El nombre de la persona mas alta es {0} y tiene {1} años, su altura es de {2}".format(nombre_max, edad_max, altura_max))
        print("4. {0}".format(cant_dias_mas_c))
        print("5. El cliente mas joven tiene {0} años, su nombre es {1} y levanta {2} kilos".format(edad_min,nombre_min,kilos_min))


    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()