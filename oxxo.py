import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def ventana_pros():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")  
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red1")
    label = tk.Label(ventana_basquet, text="Snacks", bg="red1", fg="gold2", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_snacks = [
        "1. Papas Fritas (ID: 101) - $20",
        "2. Galletas (ID: 102) - $15",
        "3. Chocolate (ID: 103) - $25",
        "4. Chicles (ID: 104) - $10",
        "5. Caramelos (ID: 105) - $5",
        "6. Nueces (ID: 106) - $30",
        "7. Pretzels (ID: 107) - $20",
        "8. Barritas Energéticas (ID: 108) - $35",
        "9. Palomitas (ID: 109) - $15",
        "10. Galletas Saladas (ID: 110) - $10"
    ]

    for producto in productos_snacks:
        frame = tk.Frame(ventana_basquet, bg="red1")
        info = tk.Label(frame, text=producto, bg="red1", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold2", fg="red", font=("Gadugi", 12), command=lambda p=producto: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def ventana_prob():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red1")
    label = tk.Label(ventana_basquet, text="Bebidas", bg="red1", fg="gold2", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_bebidas = [
        "1. Agua (ID: 201) - $10",
        "2. Refresco (ID: 202) - $20",
        "3. Jugo (ID: 203) - $15",
        "4. Té (ID: 204) - $18",
        "5. Café (ID: 205) - $25",
        "6. Leche (ID: 206) - $12",
        "7. Batido (ID: 207) - $30",
        "8. Energizante (ID: 208) - $35",
        "9. Cerveza (ID: 209) - $40",
        "10. Vino (ID: 210) - $50"
    ]

    for producto in productos_bebidas:
        frame = tk.Frame(ventana_basquet, bg="red1")
        info = tk.Label(frame, text=producto, bg="red1", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold2", fg="red", font=("Gadugi", 12), command=lambda p=producto: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def ventana_proc():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("oxxo a la vuelta de tu vida")
    ventana_basquet.geometry("400x600")
    ventana_basquet.config(background="red1")
    label = tk.Label(ventana_basquet, text="Comida", bg="red1", fg="gold2", font=("Gadugi", 16))
    label.pack(pady=10)
    
    productos_comida = [
        "1. Sándwich (ID: 301) - $50",
        "2. Ensalada (ID: 302) - $45",
        "3. Tacos (ID: 303) - $30",
        "4. Burrito (ID: 304) - $35",
        "5. Pizza (ID: 305) - $60",
        "6. Sushi (ID: 306) - $70",
        "7. Hamburguesa (ID: 307) - $55",
        "8. Hot Dog (ID: 308) - $25",
        "9. Pasta (ID: 309) - $40",
        "10. Wrap (ID: 310) - $45"
    ]

    for producto in productos_comida:
        frame = tk.Frame(ventana_basquet, bg="red1")
        info = tk.Label(frame, text=producto, bg="red1", fg="gray99", font=("Gadugi", 16))
        info.pack(side=tk.LEFT, padx=5, pady=5)
        
        boton = tk.Button(frame, text="🛒", bg="gold2", fg="red", font=("Gadugi", 12), command=lambda p=producto: agregar_producto(p))
        boton.pack(side=tk.RIGHT, padx=5, pady=5)
        
        frame.pack(fill="x")


def agregar_producto(producto):

    messagebox.showinfo("Producto agregado", f"Has agregado {producto} al carrito")


ventana = tk.Tk()
ventana.title("oxxo")
ventana.geometry("600x400")
ventana.config(background="red1", padx=0, pady=0)

header_label = tk.Label(text=" ", bg='red2', fg='gold2', font=("Century Gothic", 5))
header_label.pack(pady=0, padx=0)

header_label = tk.Label(text=" Bienvenido", bg='red2', fg='gold2', font=("Century Gothic", 40))
header_label.pack(pady=0, padx=0)

imagen = Image.open("C:\\Users\\Computo\\Desktop\\b56d5225a9edf6753d793d9b8293cca4.jpg")
imagen = imagen.resize((300, 300), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(ventana, image=imagen_tk, fg="red", bg="red")
imagen_label.pack(pady=0, padx=0)

barraMenu = tk.Menu(ventana)
ventana.config(menu=barraMenu)

mnupro = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="red", bg="gold2")
mnupro.add_command(label="Snacks", command=ventana_pros)
mnupro.add_command(label="Bebidas", command=ventana_prob)
mnupro.add_command(label="Comida", command=ventana_proc)
barraMenu.add_cascade(label="PRODUCTOS", menu=mnupro)

ventana.mainloop()
