import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Variable global para el total
total = 0

def ventana_re():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")  
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red3")
    label = tk.Label(ventana_basquet, text="Recargas", bg="red3", fg="gold3", font=("Gadugi", 16))
    label.pack(pady=10)

def ventana_ret():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")  
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red3")
    label = tk.Label(ventana_basquet, text="Retiros", bg="red3", fg="gold3", font=("Gadugi", 16))
    label.pack(pady=10)

def ventana_dep():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")  
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red3")
    label = tk.Label(ventana_basquet, text="Depositos", bg="red3", fg="gold3", font=("Gadugi", 16))
    label.pack(pady=10)

def ventana_pros():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")  
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red3")
    label = tk.Label(ventana_basquet, text="Snacks", bg="red3", fg="gold3", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_snacks = [
        ("Papas Fritas (ID: 101) - $20", 20),
        ("Galletas (ID: 102) - $15", 15),
        ("Chocolate (ID: 103) - $25", 25),
        ("Chicles (ID: 104) - $10", 10),
        ("Caramelos (ID: 105) - $5", 5),
        ("Nueces (ID: 106) - $30", 30),
        ("Pretzels (ID: 107) - $20", 20),
        ("Barritas Energéticas (ID: 108) - $35", 35),
        ("Palomitas (ID: 109) - $15", 15),
        ("Galletas Saladas (ID: 110) - $10", 10)
    ]

    for producto, precio in productos_snacks:
        frame = tk.Frame(ventana_basquet, bg="red3")
        info = tk.Label(frame, text=producto, bg="red1", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold3", fg="red3", font=("Gadugi", 12), command=lambda p=precio: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def ventana_prob():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red3")
    label = tk.Label(ventana_basquet, text="Bebidas", bg="red3", fg="gold2", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_bebidas = [
        ("Agua (ID: 201) - $10", 10),
        ("Refresco (ID: 202) - $20", 20),
        ("Jugo (ID: 203) - $15", 15),
        ("Té (ID: 204) - $18", 18),
        ("Café (ID: 205) - $25", 25),
        ("Leche (ID: 206) - $12", 12),
        ("Batido (ID: 207) - $30", 30),
        ("Energizante (ID: 208) - $35", 35),
        ("Cerveza (ID: 209) - $40", 40),
        ("Vino (ID: 210) - $50", 50)
    ]

    for producto, precio in productos_bebidas:
        frame = tk.Frame(ventana_basquet, bg="red1")
        info = tk.Label(frame, text=producto, bg="red3", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold3", fg="red3", font=("Gadugi", 12), command=lambda p=precio: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def ventana_proc():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red1")
    label = tk.Label(ventana_basquet, text="Comida", bg="red3", fg="gold2", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_comida = [
        ("Sándwich (ID: 301) - $50", 50),
        ("Ensalada (ID: 302) - $45", 45),
        ("Tacos (ID: 303) - $30", 30),
        ("Burrito (ID: 304) - $35", 35),
        ("Pizza (ID: 305) - $60", 60),
        ("Sushi (ID: 306) - $70", 70),
        ("Hamburguesa (ID: 307) - $55", 55),
        ("Hot Dog (ID: 308) - $25", 25),
        ("Pasta (ID: 309) - $40", 40),
        ("Wrap (ID: 310) - $45", 45)
    ]

    for producto, precio in productos_comida:
        frame = tk.Frame(ventana_basquet, bg="red3")
        info = tk.Label(frame, text=producto, bg="red3", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold2", fg="red3", font=("Gadugi", 12), command=lambda p=precio: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def agregar_producto(precio):
    global total
    total += precio
    messagebox.showinfo("Producto agregado", f"Has agregado un producto por ${precio}.\nTotal: ${total}")
    total_label.config(text=f"Total: ${total}")


ventana = tk.Tk()
ventana.title("oxxo")
ventana.geometry("600x500")
ventana.config(background="red3", padx=0, pady=0)

header_label = tk.Label(text=" ", bg='red3', fg='gold2', font=("Century Gothic", 5))
header_label.pack(pady=0, padx=0)

header_label = tk.Label(text=" Bienvenido", bg='red3', fg='gold2', font=("Century Gothic", 40))
header_label.pack(pady=0, padx=0)

imagen = Image.open("C:\\Users\\lupit\\Pictures\\b56d5225a9edf6753d793d9b8293cca4.jpg")
imagen = imagen.resize((300, 300), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(ventana, image=imagen_tk, fg="red3", bg="red3")
imagen_label.pack(pady=0, padx=0)

barraMenu = tk.Menu(ventana)
ventana.config(menu=barraMenu)

mnupro = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="red3", bg="gold2")
mnupro.add_command(label="Snacks🍬", command=ventana_pros)
mnupro.add_command(label="Bebidas🍔", command=ventana_prob)
mnupro.add_command(label="Comida☕️", command=ventana_proc)
barraMenu.add_cascade(label="PRODUCTOS", menu=mnupro)

mnure= tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="red3", bg="gold2")
mnure.add_command(label="📲", command=ventana_re)
barraMenu.add_cascade(label="RECARGAS", menu=mnure)

mnure= tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="red3", bg="gold2")
mnure.add_command(label="📥", command=ventana_dep)
barraMenu.add_cascade(label="DEPSITOS", menu=mnure)

mnure= tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="red3", bg="gold2")
mnure.add_command(label="📤", command=ventana_ret)
barraMenu.add_cascade(label="RETIROS", menu=mnure)

total_label = tk.Label(ventana, text="Total: $0", bg='red3', fg='gold2', font=("Century Gothic", 20))
total_label.pack(pady=10)

ventana.mainloop()
