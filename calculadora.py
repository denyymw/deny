import tkinter as tk

def boton_click(num):
    current = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, current + str(num))

def boton_clear():
    entrada.delete(0, tk.END)

def boton_igual():
    try:
        resultado = str(eval(entrada.get().replace('x', '*')))
        entrada.delete(0, tk.END)
        entrada.insert(0, resultado)
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("Calculadora ❤")
ventana.geometry("300x400")
ventana.configure(background='plum3')

entrada = tk.Entry(ventana, width=35, borderwidth=5, font=('Century Gothic', 16))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def crear_boton(texto, row, col, command):
    return tk.Button(
        ventana,
        text=texto,
        padx=20,
        pady=20,
        command=command,
        font=('Century Gothic', 16, "bold"),
        fg="hotpink4",
        bg='plum1',
        activebackground='plum3',
        
    ).grid(row=row, column=col, sticky='nsew')

boton_7 = crear_boton("7", 1, 0, lambda: boton_click(7))
boton_8 = crear_boton("8", 1, 1, lambda: boton_click(8))
boton_9 = crear_boton("9", 1, 2, lambda: boton_click(9))
boton_4 = crear_boton("4", 2, 0, lambda: boton_click(4))
boton_5 = crear_boton("5", 2, 1, lambda: boton_click(5))
boton_6 = crear_boton("6", 2, 2, lambda: boton_click(6))
boton_1 = crear_boton("1", 3, 0, lambda: boton_click(1))
boton_2 = crear_boton("2", 3, 1, lambda: boton_click(2))
boton_3 = crear_boton("3", 3, 2, lambda: boton_click(3))
boton_0 = crear_boton("0", 4, 0, lambda: boton_click(0))

boton_clear = crear_boton("C", 4, 1, boton_clear)
boton_igual = crear_boton("=", 4, 2, boton_igual)
boton_suma = crear_boton("+", 1, 3, lambda: boton_click('+'))
boton_resta = crear_boton("-", 2, 3, lambda: boton_click('-'))
boton_multi = crear_boton("x", 3, 3, lambda: boton_click('x'))
boton_divi = crear_boton("/", 4, 3, lambda: boton_click('/'))


for i in range(5):
    ventana.grid_rowconfigure(i, weight=1)
for j in range(4):
    ventana.grid_columnconfigure(j, weight=1)

ventana.mainloop()
