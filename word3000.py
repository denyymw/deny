import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, ttk

def nuevo():
    texto.delete(1.0, tk.END)
    messagebox.showinfo(title="Nuevo archivo", message="Abriendo nuevo archivo...")

def abrir():
    archivo = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if archivo:
        texto.delete(1.0, tk.END)
        with open(archivo, "r") as file:
            texto.insert(tk.END, file.read())
        messagebox.showinfo(title="Abrir archivo", message="Archivo abierto exitosamente")

def guardar():
    archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", ".txt"), ("All Files", ".*")])
    if archivo:
        with open(archivo, "w") as file:
            file.write(texto.get(1.0, tk.END))
        messagebox.showinfo(title="Guardar", message="Archivo guardado exitosamente")

def cerrar():
    ventana.quit()

def cambiar_fuente():
    fuentes = ["Helvetica", "Times", "Courier", "Arial"]
    seleccion = tk.StringVar()
    seleccion.set(fuentes[0])
    ventana_fuente = tk.Toplevel()
    ventana_fuente.title("Cambiar Fuente")
    tk.Label(ventana_fuente, text="Seleccione la fuente:").pack(pady=10)
    menu_fuentes = ttk.Combobox(ventana_fuente, textvariable=seleccion, values=fuentes)
    menu_fuentes.pack(pady=10)
    def aplicar_fuente():
        texto.config(font=(seleccion.get(), 12))
        ventana_fuente.destroy()
    boton_aplicar = tk.Button(ventana_fuente, text="Aplicar", command=aplicar_fuente)
    boton_aplicar.pack(pady=10)

def cambiar_color():
    color = colorchooser.askcolor()[1]
    if color:
        texto.config(fg=color)

def poner_negritas():
    try:
        texto.tag_configure("negritas", font=(texto.cget("font").split()[0], 12, "bold"))
        current_tags = texto.tag_names("sel.first")
        if "negritas" in current_tags:
            texto.tag_remove("negritas", "sel.first", "sel.last")
        else:
            texto.tag_add("negritas", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showerror("Error", "Selecciona el texto que quieres poner en negritas.")

def poner_subrayado():
    try:
        texto.tag_configure("subrayado", font=(texto.cget("font").split()[0], 12, "underline"))
        current_tags = texto.tag_names("sel.first")
        if "subrayado" in current_tags:
            texto.tag_remove("subrayado", "sel.first", "sel.last")
        else:
            texto.tag_add("subrayado", "sel.first", "sel.last")
    except tk.TclError:
        messagebox.showerror("Error", "Selecciona el texto que quieres subrayar.")

def cambiar_tamano():
    ventana_tamano = tk.Toplevel()
    ventana_tamano.title("Cambiar Tamaño del Texto")
    tk.Label(ventana_tamano, text="Seleccione el tamaño:").pack(pady=10)
    spinbox_tamano = tk.Spinbox(ventana_tamano, from_=8, to=72)
    spinbox_tamano.pack(pady=10)
    def aplicar_tamano():
        texto.config(font=(texto.cget("font").split()[0], int(spinbox_tamano.get())))
        ventana_tamano.destroy()
    boton_aplicar = tk.Button(ventana_tamano, text="Aplicar", command=aplicar_tamano)
    boton_aplicar.pack(pady=10)

ventana = tk.Tk()
ventana.title("wordeny")
ventana.geometry("600x400")

header = tk.Frame(ventana, bg='blue', height=40)
header.pack(fill=tk.X)

header_label = tk.Label(header, text="Documento", bg='blue', fg='chartreuse1', font=("Century Gothic", 14))
header_label.pack(pady=5)

barraMenu = tk.Menu(ventana, font=("Century Gothic", 12))
ventana.config(menu=barraMenu)

mnuArchivo = tk.Menu(barraMenu, tearoff=0, font=("Century Gothic", 12))
mnuArchivo.add_command(label="Nuevo", command=nuevo)
mnuArchivo.add_command(label="Abrir", command=abrir)
mnuArchivo.add_separator()
mnuArchivo.add_command(label="Guardar como", command=guardar)
mnuArchivo.add_command(label="Cerrar", command=cerrar)

mnuInicio = tk.Menu(barraMenu, tearoff=0, font=("Century Gothic", 12))
mnuInicio.add_command(label="Cambiar Fuente", command=cambiar_fuente)
mnuInicio.add_command(label="Cambiar Color", command=cambiar_color)
mnuInicio.add_command(label="Negritas", command=poner_negritas)
mnuInicio.add_command(label="Subrayar", command=poner_subrayado)
mnuInicio.add_command(label="Cambiar Tamaño", command=cambiar_tamano)  # Opción para cambiar tamaño

mnux = tk.Menu(barraMenu, tearoff=0, font=("Century Gothic", 12))
mnux.add_command(label="Aun no esta abilitada")

barraMenu.add_cascade(label="Archivo", menu=mnuArchivo)
barraMenu.add_cascade(label="Inicio", menu=mnuInicio)
barraMenu.add_cascade(label="Diseño", menu=mnux)
barraMenu.add_cascade(label="Disposicio", menu=mnux)
barraMenu.add_cascade(label="Referncias", menu=mnux)
barraMenu.add_cascade(label="Correspondencia", menu=mnux)
barraMenu.add_cascade(label="Revisar", menu=mnux)
barraMenu.add_cascade(label="Vista", menu=mnux)
barraMenu.add_cascade(label="Ayuda", menu=mnux)

texto = tk.Text(ventana, width=60, height=80)
texto.config(bg='ghost white', bd=1, relief="solid", font=("Century Gothic", 12))
texto.pack(pady=40)

ventana.mainloop()