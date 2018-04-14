from tkinter import *
from tkinter.ttk import *
import sqlite3
import re

#Create by Juandeyby

raiz=Tk()
raiz.title("Agenta de contactos 1.0")
raiz.resizable(0, 0)
raiz.iconbitmap("logo.ico")
miFrame=Frame()
miFrame.grid(row=0, column=0, sticky="n")

id_string=StringVar()
nombre_string=StringVar()
apellido_string=StringVar()
correo_string=StringVar()
telefono_string=StringVar()
estado_string=StringVar()

registro_label=Label(miFrame, text="REGISTRO").grid(row=0, column=0, sticky="w", padx=5, pady=5)
id_label=Label(miFrame, text="ID :").grid(row=1, column=0, sticky="w", padx=5, pady=5)
nombre_label=Label(miFrame, text="Nombre :").grid(row=2, column=0, sticky="w", padx=5, pady=5)
apellido_label=Label(miFrame, text="Apellido :").grid(row=3, column=0, sticky="w", padx=5, pady=5)
correo_label=Label(miFrame, text="Correo :").grid(row=4, column=0, sticky="w", padx=5, pady=5)
telefono_label=Label(miFrame, text="Telefono o celular:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
estado_civil_label=Label(miFrame, text="Estado civil :").grid(row=6, column=0, sticky="w", padx=5, pady=5)
estado_label=Label(miFrame, textvariable=estado_string)
estado_label.grid(row=14, column=0, columnspan=3, sticky="w")

id_label=Entry(miFrame, textvariable=id_string, width=5)
id_label.grid(row=1, column=1, sticky="w", padx=5, pady=5)
id_label.config(state='readonly')
nombre_entry=Entry(miFrame, textvariable=nombre_string, width=23)
nombre_entry.grid(row=2, column=1, sticky="w", padx=5, pady=5, columnspan=2)
apellido_entry=Entry(miFrame, textvariable=apellido_string, width=23)
apellido_entry.grid(row=3, column=1, sticky="w", padx=5, pady=5, columnspan=2)
correo_entry=Entry(miFrame, textvariable=correo_string, width=23).grid(row=4, column=1, sticky="w", padx=5, pady=5, columnspan=2)
telefono_entry=Entry(miFrame, textvariable=telefono_string, width=23).grid(row=5, column=1, sticky="w", padx=5, pady=5, columnspan=2)
estado_civil=Combobox(miFrame, state="readonly", width=20)
estado_civil.grid(row=6, column=1, sticky="w", padx=5, pady=5, columnspan=2)

#registro_label=Label(miFrame2, text="LISTA DE USUARIOS").grid(row=0, column=0, sticky="w", padx=5, pady=5)

lista_label=Label(miFrame, text="LISTA").grid(row=0, column=3, sticky="w", padx=5, pady=5)
listbox=Listbox(miFrame)
listbox.grid(row=1, column=3, rowspan=6, padx=5, pady=5)

informacion_label=Label(miFrame, text="INFORMACION").grid(row=8, column=0, sticky="w", padx=5, pady=0)
nombre_label_info=Label(miFrame, text="Nombre :").grid(row=9, column=1, sticky="w", padx=5, pady=0)
apellido_label_info=Label(miFrame, text="Apellido :").grid(row=10, column=1, sticky="w", padx=5, pady=0)
correo_label_info=Label(miFrame, text="Correo :").grid(row=11, column=1, sticky="w", padx=5, pady=0)
telefono_label_info=Label(miFrame, text="Telefono :").grid(row=12, column=1, sticky="w", padx=5, pady=0)
estado_civil_label_info=Label(miFrame, text="Estado civil :").grid(row=13, column=1, sticky="w", padx=5, pady=0)

nombre_info_string=StringVar()
apellido_info_string=StringVar()
correo_info_string=StringVar()
telefono_info_string=StringVar()
estado_civil_info_string=StringVar()

nombre_info=Label(miFrame, textvariable=nombre_info_string).grid(row=9, column=2, sticky="w", padx=5, pady=0, columnspan=2)
apellido_info=Label(miFrame, textvariable=apellido_info_string).grid(row=10, column=2, sticky="w", padx=5, pady=0, columnspan=2)
correo_info=Label(miFrame, textvariable=correo_info_string).grid(row=11, column=2, sticky="w", padx=5, pady=0, columnspan=2)
telefono_info=Label(miFrame, textvariable=telefono_info_string).grid(row=12, column=2, sticky="w", padx=5, pady=0, columnspan=2)
estado_civil_info=Label(miFrame, textvariable=estado_civil_info_string).grid(row=13, column=2, sticky="w", padx=5, pady=0, columnspan=2)
img=PhotoImage(file='photo.png')
img_info=Label(miFrame, image=img)
img_info.grid(row=9, column=0, rowspan=5, sticky=W+E+N+S, padx=10, pady=5)

def mostrar_lista(estado_civil):
    com_bd = sqlite3.connect('usuarios.bd')
    cursor_agenda = com_bd.cursor()
    #Lleado del combo box
    cursor_agenda.execute("SELECT * FROM estado_civil")
    list=[]
    for regitro in cursor_agenda:
        list.append(regitro[1])
    estado_civil["values"]=list
    #Llenado de la lista
    cursor_agenda.execute("SELECT * FROM usuario")
    for regitro in cursor_agenda:
        listbox.insert(END, regitro[1])
    print("Lista Exitoso!")

def registrar(estado_civil):
    if re.compile("^([A-zñáéíóú]{2,60}[\s]?)+$").match(nombre_string.get()) is None:
        estado_string.set("Estado: Formato incorrecto NOMBRE")
        estado_label.config(foreground="red")
    elif re.compile("^([A-zñáéíóú]{2,60}[\s]?)+$").match(apellido_string.get()) is None:
        estado_string.set("Estado: Formato incorrecto APELLIDO")
        estado_label.config(foreground="red")
    elif re.compile("^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$").match(correo_string.get()) is None:
        estado_string.set("Estado: Formato incorrecto CORREO")
        estado_label.config(foreground="red")
    elif re.compile("^([0-9]{9}?)+$").match(telefono_string.get()) is None:
        estado_string.set("Estado: Numero de TELEFONO incorrecto, ingrese 9 digitos")
        estado_label.config(foreground="red")
    else:
        com_bd=sqlite3.connect('usuarios.bd')
        cursor_agenda=com_bd.cursor()
        #Estado civil
        cursor_agenda.execute("SELECT * FROM estado_civil")
        estado_civil_value=-1
        list=[]
        for regitro in cursor_agenda:
            list.append(regitro[1])
        for i in range(len(list)):
            if estado_civil.get() == list[i]:
                estado_civil_value = i+1 # restar -1 porque SQLITE comienza desde 1 y no desde 0
        reg=(nombre_string.get(), apellido_string.get(), correo_string.get(), telefono_string.get(), estado_civil_value)
        #cursor_agenda.execute("CREATE TABLE estado_civil (id INTEGER PRIMARY KEY AUTOINCREMENT, "
        #                      "nombre VARCHAR(30) UNIQUE)")
        #cursor_agenda.execute("CREATE TABLE usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre VARCHAR(30) UNIQUE,"
        #                      "apellido VARCHAR(40), estado_civil INTEGER, correo VARCHAR(40), telefono INT(9),"
        #                      "FOREIGN KEY (estado_civil) REFERENCES estado_civil(nombre))")
        #cursor_agenda.execute("INSERT INTO estado_civil (nombre) VALUES('soltero')")
        #cursor_agenda.execute("INSERT INTO estado_civil (nombre) VALUES('casado')")
        #cursor_agenda.execute("INSERT INTO estado_civil (nombre) VALUES('divorciado')")
        #cursor_agenda.execute("INSERT INTO estado_civil (nombre) VALUES('viudo')")
        try:
            cursor_agenda.execute("INSERT INTO usuario (nombre, apellido, correo, telefono, estado_civil) VALUES(?, ?, ?, ?, ?)", reg)
        except sqlite3.IntegrityError:
            estado_string.set("Estado: Ya existe usuario")
            estado_label.config(foreground="red")
            return
        com_bd.commit()
        cursor_agenda.execute("SELECT * FROM usuario")
        listbox.delete(0, END)
        for regitro in cursor_agenda:
            listbox.insert(END, regitro[1])
        nombre_string.set("")
        apellido_string.set("")
        correo_string.set("")
        telefono_string.set("")
        estado_civil.set("")
        estado_string.set("Estado: Resgistro exitoso")
        estado_label.config(foreground="green")

def seleccionar(e):
    com_bd = sqlite3.connect('usuarios.bd')
    cursor_agenda = com_bd.cursor()
    #cursor_agenda.execute("SELECT * FROM usuario")
    #cursor_agenda.execute("SELECT usuario.nombre, apellido, correo, telefono, estado_civil.nombre "
    cursor_agenda.execute("SELECT usuario.nombre, apellido, correo, telefono, estado_civil.nombre "
                          "FROM usuario INNER JOIN estado_civil ON usuario.estado_civil = estado_civil.id")
    list=[]
    for regitro in cursor_agenda:
        list.append(regitro)
    index=listbox.curselection()
    if index == ():
        print("Lista no seleccionada")
    else:
        selecionado=list[index[0]]
        nombre_info_string.set(selecionado[0])
        apellido_info_string.set(selecionado[1])
        correo_info_string.set(selecionado[2])
        telefono_info_string.set(selecionado[3])
        estado_civil_info_string.set(selecionado[4])
        estado_string.set("Estado: Destalles del contacto")
        estado_label.config(foreground="green")

def eliminar():
    com_bd = sqlite3.connect('usuarios.bd')
    cursor_agenda = com_bd.cursor()
    cursor_agenda.execute("SELECT usuario.nombre, apellido, correo, telefono, estado_civil.nombre "
                          "FROM usuario INNER JOIN estado_civil ON usuario.estado_civil = estado_civil.id")
    list=[]
    for regitro in cursor_agenda:
        list.append(regitro)
    index=listbox.curselection()
    if index == ():
        print("Lista no seleccionado")
    else:
        #selecionado=list[index[0]]
        cursor_agenda.execute("DELETE FROM usuario WHERE nombre == '" + listbox.get(index[0]) + "'")
        com_bd.commit()
        cursor_agenda.execute("SELECT * FROM usuario")
        listbox.delete(0, END)
        for regitro in cursor_agenda:
            listbox.insert(END, regitro[1])
        estado_string.set("Estado: Borrado exitoso")
        estado_label.config(foreground="green")

def cargar():
    com_bd = sqlite3.connect('usuarios.bd')
    cursor_agenda = com_bd.cursor()
    index=listbox.curselection()
    if index == ():
        print("Lista no seleccionado")
    else:
        cursor_agenda.execute("SELECT usuario.id, usuario.nombre, apellido, correo, telefono, estado_civil.nombre "
                          "FROM usuario INNER JOIN estado_civil ON usuario.estado_civil = estado_civil.id "
                              "and usuario.nombre = '" + listbox.get(index[0]) + "' ")
        list=[]
        for regitro in cursor_agenda:
            list = regitro
        id_string.set(list[0])
        nombre_string.set(list[1])
        apellido_string.set(list[2])
        correo_string.set(list[3])
        telefono_string.set(list[4])
        estado_civil.set(list[5])
        estado_string.set("Estado: Contacto cargado")
        estado_label.config(foreground="green")

def modificar():
    com_bd = sqlite3.connect('usuarios.bd')
    cursor_agenda = com_bd.cursor()
    # Estado civil
    cursor_agenda.execute("SELECT * FROM estado_civil")
    estado_civil_value = -1
    list = []
    for regitro in cursor_agenda:
        list.append(regitro[1])
    for i in range(len(list)):
        if estado_civil.get() == list[i]:
            estado_civil_value = i + 1
    reg = (nombre_string.get(), apellido_string.get(), correo_string.get(), telefono_string.get(),
           estado_civil_value, id_string.get())
    cursor_agenda.execute(
        "UPDATE usuario SET nombre = ?, apellido = ?, correo = ?, telefono = ?, estado_civil = ? WHERE id == ?", reg)
    com_bd.commit()
    cursor_agenda.execute("SELECT * FROM usuario")
    listbox.delete(0, END)
    for regitro in cursor_agenda:
        listbox.insert(END, regitro[1])
    id_string.set("")
    nombre_string.set("")
    apellido_string.set("")
    correo_string.set("")
    telefono_string.set("")
    estado_civil.set("")
    estado_string.set("Estado: Modificacion exitosa")
    estado_label.config(foreground="green")

def limpiar():
    id_string.set("")
    nombre_string.set("")
    apellido_string.set("")
    correo_string.set("")
    telefono_string.set("")
    estado_civil.set("")
    estado_string.set("Estado: Compos limpios")
    estado_label.config(foreground="green")

listbox.bind('<<ListboxSelect>>', seleccionar)

button_Frame=Frame(miFrame)
button_Frame.grid(row=7, column=0, columnspan=4)

registrar_button=Button(button_Frame, text="Registrar", command=lambda : registrar(estado_civil))
registrar_button.grid(row=0, column=0, padx=5, pady=5)

modificar_button=Button(button_Frame, text="Modificar", command=modificar)
modificar_button.grid(row=0, column=1, padx=5, pady=5)

eliminar_button=Button(button_Frame, text="Eliminar", command=eliminar)
eliminar_button.grid(row=0, column=2, padx=5, pady=5)

cargar_button=Button(button_Frame, text="Cargar", command=cargar)
cargar_button.grid(row=0, column=3, padx=5, pady=5)

cargar_button=Button(button_Frame, text="Limpiar", command=limpiar)
cargar_button.grid(row=0, column=4, padx=5, pady=5)

mostrar_lista(estado_civil)
raiz.mainloop()
