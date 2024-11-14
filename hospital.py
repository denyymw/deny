import tkinter as tk

ventana = tk.Tk()
ventana.title("Control Hospital")
ventana.geometry("600x500")
ventana.config(background="lightBlue", padx=0, pady=0)


def ventana_Cardiología():
    ventana_Cardiología = tk.Toplevel() 
    ventana_Cardiología.title("Cardiología")
    ventana_Cardiología.geometry("400x500")
    ventana_Cardiología.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Cardiología: Esta abarca lo relacionado con el sistema cardiovascular. "
             "Este médico especialista se encarga del estudio, diagnóstico y tratamiento "
             "de todas las enfermedades que afectan al corazón y al aparato circulatorio de las personas.")
             
    text_widget = tk.Text(ventana_Cardiología, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')
    


def ventana_Neurología():
    ventana_Neurología= tk.Toplevel() 
    ventana_Neurología.title("Neurología")
    ventana_Neurología.geometry("400x500")
    ventana_Neurología.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Neurología:La neurología es la especialidad médica que tiene competencia en el estudio del sistema nervioso, y de las enfermedades del cerebro" 
             "la médula, los nervios periféricos y los músculos. La neurología ha sido considerada por algunos la especialidad clínica por excelencia.")
             
    text_widget = tk.Text(ventana_Neurología, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')

def ventana_Gastroenterología():
    ventana_Gastroenterología= tk.Toplevel() 
    ventana_Gastroenterología.title("Gastroenterología")
    ventana_Gastroenterología.geometry("400x500")
    ventana_Gastroenterología.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Gastroenterología:La gastroenterología es el estudio de la función normal y las enfermedades del esófago, estómago, intestino delgado, colon y recto, páncreas, vesícula biliar, conductos biliares e hígado.")
             
    text_widget = tk.Text(ventana_Gastroenterología, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')


def ventana_Pediatría():
    ventana_Pediatría= tk.Toplevel() 
    ventana_Pediatría.title("Pediatría")
    ventana_Pediatría.geometry("400x500")
    ventana_Pediatría.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Pediatría:¿Qué es la pediatría? La pediatría es una rama de la medicina especializada en el desarrollo, el cuidado y las afecciones de la salud propias de bebés, niños y adolescentes.")
             
    text_widget = tk.Text(ventana_Pediatría, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')


def ventana_Cirugía_Pediátrica():
    ventana_Cirugía_Pediátrica= tk.Toplevel() 
    ventana_Cirugía_Pediátrica.title("Cirugía Pediátrica")
    ventana_Cirugía_Pediátrica.geometry("400x500")
    ventana_Cirugía_Pediátrica.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Cirugía Pediátrica: La Cirugía Pediátrica es la especialidad que se encarga del estudio, diagnóstico y tratamiento de las enfermedades quirúrgicas, congénitas y adquiridas, del feto, recién nacido, lactante, escolar y adolescente, hasta los 18 años de edad")
             
    text_widget = tk.Text(ventana_Cirugía_Pediátrica, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')


def ventana_Cirugía_General():
    ventana_Cirugía_General= tk.Toplevel() 
    ventana_Cirugía_General.title("Cirugía General")
    ventana_Cirugía_General.geometry("400x500")
    ventana_Cirugía_General.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Cirugía General:Rama de la cirugía que cubre las áreas principales de tratamientos quirúrgicos. Los cirujanos generales tratan las enfermedades del abdomen, la mama, la cabeza y el cuello, los vasos sanguíneos y el aparato digestivo.")
             
    text_widget = tk.Text(ventana_Cirugía_General, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')

def ventana_Dermatología():
    ventana_Dermatología= tk.Toplevel() 
    ventana_Dermatología.title("Dermatología:Los dermatólogos lo ayudan a mantener la piel saludable mediante el tratamiento de enfermedades y afecciones cutáneas cotidianas, como erupciones cutáneas, acné, psoriasis y rosácea, tanto en pacientes pediátricos como en pacientes adultos.")
    ventana_Dermatología.geometry("400x500")
    ventana_Dermatología.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Dermatología:Los dermatólogos lo ayudan a mantener la piel saludable mediante el tratamiento de enfermedades y afecciones cutáneas cotidianas, como erupciones cutáneas, acné, psoriasis y rosácea, tanto en pacientes pediátricos como en pacientes adultos.")
             
    text_widget = tk.Text(ventana_Dermatología, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')

def ventana_Medicina_estética():
    ventana_Medicina_estética= tk.Toplevel() 
    ventana_Medicina_estética.title("Medicina estética")
    ventana_Medicina_estética.geometry("400x500")
    ventana_Medicina_estética.config(background="lightBlue")

    #para que el texto se vea de bien
    texto = ("Medicina estética:La medicina estética es el área de la medicina que se centra en mejorar y mantener el bienestar y la apariencia física de los pacientes. Para esto, aplica diferentes procedimientos y tratamientos no quirúrgicos y mínimamente invasivos.")
             
    text_widget = tk.Text(ventana_Medicina_estética, bg="lightBlue", fg="BLACK", font=("ADLaM Display", 14), padx=10, pady=10)
    text_widget.insert(tk.END, texto)
    text_widget.config(state=tk.DISABLED)
    text_widget.pack(expand=True, fill='both')

def ventana_P():
    ventana.destroy()
    ventana_p = tk.Tk() 
    ventana_p.title("Hospital")
    ventana_p.geometry("600x500")
    ventana_p.config(background="lightBlue")
    label = tk.Label(ventana_p, text="Bienvenidos CDHDA", bg="lightBlue", fg="BLACK", font=("Gadugi", 16))
    label.pack(pady=10)

    barraMenu = tk.Menu(ventana_p)
    ventana_p.config(menu=barraMenu)
    mnu0 = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="lightBlue", bg="white")
    mnu0.add_command(label="Cardiología", command=ventana_Cardiología)
    mnu0.add_command(label="Neurología",command=ventana_Neurología)
    barraMenu.add_cascade(label="Hospital de la Paz", menu=mnu0)
   
    mnu1 = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="lightBlue", bg="white")
    mnu1.add_command(label="Gastroenterología",command=ventana_Gastroenterología)
    mnu1.add_command(label="Pediatría",command=ventana_Pediatría)
    barraMenu.add_cascade(label="Hospital DS ", menu=mnu1)

    mnu2 = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="lightBlue", bg="white")
    mnu2.add_command(label="Cirugía Pediátrica",command=ventana_Cirugía_Pediátrica)
    mnu2.add_command(label="Cirugía General",command=ventana_Cirugía_General)
    barraMenu.add_cascade(label="Hospital concordia", menu=mnu2)

    mnu3 = tk.Menu(barraMenu, tearoff=0, font=("", 15), fg="lightBlue", bg="white")
    mnu3.add_command(label="Dermatología",command=ventana_Dermatología)
    mnu3.add_command(label="Medicina estética",command=ventana_Medicina_estética)
    barraMenu.add_cascade(label="Hospital sonia", menu=mnu3)

label_username = tk.Label(ventana, text="Nombre:", bg="lightBlue", fg="black")
label_username.pack(pady=5)
entry_username = tk.Entry(ventana)
entry_username.pack(pady=5)

label_password = tk.Label(ventana, text="Contraseña:", bg="lightBlue", fg="black")
label_password.pack(pady=5)
entry_password = tk.Entry(ventana, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(ventana, text="Siguiente", command=ventana_P, bg="#008CBA", fg="white")
button_login.pack(pady=20)

ventana.mainloop()
