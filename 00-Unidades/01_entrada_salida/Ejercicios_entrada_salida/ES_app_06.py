import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Adan
apellido: Gonzalez
---
Ejercicio: entrada_salida_06
---
Enunciado:
Al presionar el botón  'Sumar', se deberán obtener los valores contenidos en las cajas de texto (txt_operador_A y txt_operador_B), transformarlos en números enteros, realizar la suma y luego mostrar el resultado de la operación utilizando el Dialog Alert. 
Ej: "El resultado de la sumas es: 755" 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Operador A")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_operador_a = customtkinter.CTkEntry(master=self)
        self.txt_operador_a.grid(row=0, column=1)
        
        self.label2 = customtkinter.CTkLabel(master=self, text="Operador B")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_operador_b = customtkinter.CTkEntry(master=self)
        self.txt_operador_b.grid(row=1, column=1)
        
        self.btn_sumar = customtkinter.CTkButton(master=self, text="Sumar", command=self.btn_sumar_on_click)
        self.btn_sumar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_sumar_on_click(self):
        pass
        Num_1 = self.txt_operador_a.get()
        Num_1_N = int(Num_1)

        Num_2 = self.txt_operador_b.get()
        Num_2_N = int(Num_2)

        Resultado = Num_1_N + Num_2_N
        #Num_Texto = str(Resultado)

        Mensaje = "El resultado es {0}".format(Resultado)
        #Mensaje = "El resultado es " + Num_Texto
        
        alert("EJ 6", Mensaje )


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()


    '''


    si la suma no se muestra en el alert al usar el + , se debe de volver al texto con str()
    
    el numero se puede convertir en numero en una sola linea ya q poniendo el int antes del self.txt_operador_a.get() se trans forma en un numero

    string = cadena de carectos             convertir a texto   str(resulto)
    int = numeros enteros                   convertir a numeros int(numero_uno)
    float = numeros decimales               convertir a decimal float(numero_uno)

    El = sirver para  asignar

    El + sirve ára sumar y concatenar

    El - siver para restar

    El * sirve para  multiplicar

    El 7 sirve para dividir
    
    El % sirve para mostrar el resto de una divicion ( es el modulo)
    
    '''