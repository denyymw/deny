import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def ventana_basquet():
    ventana_basquet = tk.Toplevel()
    ventana_basquet.title("Centro cultural")
    ventana_basquet.geometry("400x300")
    ventana_basquet.config(background="gray11")
    label = tk.Label(ventana_basquet, text="Información sobre Basquet", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_basquet, text="El basquetbol es un deporte de equipo.\nHorarios: Lunes y Miércoles de 16:00 a 18:00")
    info.pack(pady=10)

def ventana_voly():
    ventana_voly = tk.Toplevel()
    ventana_voly.title("Centro cultural")
    ventana_voly.geometry("400x300")
    ventana_voly.config(background="gray11")
    label = tk.Label(ventana_voly, text="Información sobre Voley", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_voly, text="El voleibol es un deporte de equipo.\nHorarios: Martes y Jueves de 17:00 a 19:00")
    info.pack(pady=10)

def ventana_ame():
    ventana_ame = tk.Toplevel()
    ventana_ame.title("Centro cultural")
    ventana_ame.geometry("400x300")
    ventana_ame.config(background="gray11")
    label = tk.Label(ventana_ame, text="Información sobre Football Americano", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_ame, text="El fútbol americano es un deporte.\nHorarios: Viernes de 16:00 a 18:00")
    info.pack(pady=10)

def ventana_pintura():
    ventana_pintura = tk.Toplevel()
    ventana_pintura.title("Centro cultural")
    ventana_pintura.geometry("400x300")
    ventana_pintura.config(background="gray11")
    label = tk.Label(ventana_pintura, text="Información sobre Pintura", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_pintura, text="La pintura es una forma de arte.\nHorarios: Lunes y Miércoles de 14:00 a 16:00")
    info.pack(pady=10)

def ventana_dibujo():
    ventana_dibujo = tk.Toplevel()
    ventana_dibujo.title("Centro cultural")
    ventana_dibujo.geometry("400x300")
    ventana_dibujo.config(background="gray11")
    label = tk.Label(ventana_dibujo, text="Información sobre Dibujo", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_dibujo, text="El dibujo es una técnica artística.\nHorarios: Martes y Jueves de 14:00 a 16:00")
    info.pack(pady=10)

def ventana_danza():
    ventana_danza = tk.Toplevel()
    ventana_danza.title("Centro cultural")
    ventana_danza.geometry("400x300")
    ventana_danza.config(background="gray11")
    label = tk.Label(ventana_danza, text="Información sobre Danza", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_danza, text="La danza es una forma de expresión.\nHorarios: Viernes de 17:00 a 19:00")
    info.pack(pady=10)

def ventana_literatura():
    ventana_literatura = tk.Toplevel()
    ventana_literatura.title("Centro cultural")
    ventana_literatura.geometry("400x300")
    ventana_literatura.config(background="gray11")
    label = tk.Label(ventana_literatura, text="Información sobre Literatura", font=("Gadugi", 16))
    label.pack(pady=20)
    info = tk.Label(ventana_literatura, text="La literatura abarca obras escritas.\nHorarios: Miércoles de 16:00 a 18:00")
    info.pack(pady=10)

def ventana_con():
    ventana_con = tk.Toplevel()
    ventana_con.title("Centro cultural")
    ventana_con.geometry("400x300")
    ventana_con.config(background="gray11")
    label = tk.Label(ventana_con, text="Llámanos al 4493942166 o búscanos en Instagram como denyymw", font=("Gadugi", 16))
    label.pack(pady=30)

def ventana_su():
    ventana_su = tk.Toplevel()
    ventana_su.title("Centro cultural")
    ventana_su.geometry("400x300")
    ventana_su.config(background="gray11")
    label = tk.Label(ventana_su, text="Búscanos en la calle Villa Muro #156 y en la calle Colina de las Margaritas #43", font=("Gadugi", 16))
    label.pack(pady=30)

def ventana_login():
    ventana_login = tk.Toplevel()
    ventana_login.title("Crear cuenta")
    ventana_login.geometry("400x300")
    ventana_login.config(background="gray11")
    tk.Label(ventana_login, text="Crear cuenta", font=("Gadugi", 16), bg="gray11", fg="white").pack(pady=10)
    tk.Label(ventana_login, text="Usuario:", bg="white").pack(pady=5)
    user_entry = tk.Entry(ventana_login)
    user_entry.pack(pady=5)
    tk.Label(ventana_login, text="Contraseña:", bg="white").pack(pady=5)
    pass_entry = tk.Entry(ventana_login, show="*")
    pass_entry.pack(pady=5)
    
    def registrar():
        usuario = user_entry.get()
        contraseña = pass_entry.get()
        if usuario and contraseña:
            messagebox.showinfo("Registro exitoso", f"Usuario {usuario} registrado con éxito.")
            ventana_login.destroy()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
    
    tk.Button(ventana_login, text="Registrar", command=registrar, bg="white", fg="gray11", font=("Gadugi", 12), relief=tk.FLAT).pack(pady=10)

ventana = tk.Tk()
ventana.title("Centro cultural")
ventana.geometry("600x400")
ventana.config(background="gray11", padx=0, pady=0)

header_label = tk.Label(text="Centro cultural Dni", bg='gray11', fg='green3', font=("Informal Roman", 40))
header_label.pack(pady=0, padx=0)

imagen = Image.open("C:\\Users\\lupit\\Desktop\\7bfb2e449ffff6b78f5cb76cd4dca01f.jpg")
imagen = imagen.resize((500, 400), Image.LANCZOS)
imagen_tk = ImageTk.PhotoImage(imagen)
imagen_label = tk.Label(ventana, image=imagen_tk, bg='gray10')
imagen_label.pack(pady=0, padx=0)

barraMenu = tk.Menu(ventana, fg="purple4")
ventana.config(menu=barraMenu)

mnuAc = tk.Menu(barraMenu, tearoff=0)
mnuAc.add_command(label="Basquet", command=ventana_basquet)
mnuAc.add_separator()
mnuAc.add_command(label="Voley", command=ventana_voly)
mnuAc.add_separator()
mnuAc.add_command(label="Football Americano", command=ventana_ame)
mnuAc.add_separator()
mnuAc.add_command(label="Pintura", command=ventana_pintura)
mnuAc.add_separator()
mnuAc.add_command(label="Dibujo", command=ventana_dibujo)
mnuAc.add_separator()
mnuAc.add_command(label="Danza", command=ventana_danza)
mnuAc.add_separator()
mnuAc.add_command(label="Literatura", command=ventana_literatura)
barraMenu.add_cascade(label="Actividades", menu=mnuAc)

mnucon = tk.Menu(barraMenu, tearoff=0)
mnucon.add_command(label="Contactos", command=ventana_con)
mnucon.add_command(label="Sucursales", command=ventana_su)
barraMenu.add_cascade(label="Datos", menu=mnucon)

mnuini = tk.Menu(barraMenu, tearoff=0)
mnuini.add_command(label="Crear cuenta", command=ventana_login)
barraMenu.add_cascade(label="Crea tu cuenta", menu=mnuini)

ventana.mainloop()
