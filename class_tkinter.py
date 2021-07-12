#Paso 1 instalacion de la librería

#Paso 2 importar librería y crear ventana principal y su mainloop()

from tkinter import *

main_window = Tk()         #Ventana principal de la aplicación
main_window.title("Formulario de registro")
#main_window.mainloop()     #Abre la ventana y entra en un loop que permite tener la interfaz abierta en la ejecución

#Paso 3. Creación de Frames

#Frames / Marcos -> permiten agrupar contenido
main_frame = Frame(main_window,     #Ventana donde se pondra el frame
                   bg='#FFFFFF',    #background color, codigo html con el color
                   height = 500,    #alto
                   width = 500,     #ancho
                   padx = 50,       #margen en el eje x
                   pady = 50,       #margen en el eje y
                   cursor='arrow')  #que figura tiene el cursor -> dot, arrow

main_frame.pack()       #se instancia en la interfaz (se pone)
#main_window.mainloop()  #Toda la creación de interfaces debe estar entre main_window= TK() y .mainloop()

#Paso 4. Labels -> Se utiliza para escribir texto, títulos, etiquetas de botones, etc

title_label = Label(main_frame,        #frame donde se ubica el Label
                    text = "Formulario de registro",    #texto a visualizar en el label
                    font=('Arial',11),          #Tipo de letra y tamañO
                    fg = '#000000',             #Color de la letra
                    justify = CENTER)           #Alineación LEFT, RIGHT, CENTER

title_label.pack()
#main_window.mainloop()

#Paso 5. PhotoImage -> Insertar imagenes en el Frame que se esta trabajando

imagen = PhotoImage(file='register_form.png')
img_label = Label(main_frame, #frame donde se ubica el Label
                  image=imagen)       #path de la imagen a visualizar
img_label.pack()
#main_window.mainloop()

#Paso 6. Button -> Botones

boton = Button(main_frame, text = "Click")
boton.pack()
#main_window.mainloop()

def accion():
    global boton_text
    if boton_text == "Click":
        boton_text = "Le dió click"
    else:
        boton_text = "Click"
    boton.config(text=boton_text)

#acciones en un boton
boton_text = "Click"            #Se debe crear una variable para almacenar el texto
boton = Button(main_frame, text =boton_text, command = accion)
boton.pack()
#main_window.mainloop()

#Paso 7 -> Posicionamiento  se utiliza .place(x = posX, y = posY)

ventana = Tk()
ventana.title("Posicionamiento")
ventana.geometry("400x200")
boton = Button(ventana, text = "Primer Widget").place(x=10, y=10)
etiqueta = Label(ventana, text="Segundo Widget").place(x=200, y=10)
etiqueta2 = Label(ventana, text="Tercer Widget").place(x=10, y=30)
etiqueta3 = Label(ventana, text="Cuarto Widget").place(x=200, y=30)
#ventana.mainloop()

#Ejercicio Paint -> haciendo clic "Dame clic para saludar" muestra el mensaje "Hola a todos
#haciendo clic para minimizar la ventana se minimiza

def saludo():
    print("Hola a todos")

def minimizar():
    ventana.iconify()

ventana = Tk()
ventana.title("Ejercicio Numero 1")
ventana.geometry("400x200")
etiqueta1 = Label(ventana, text = "Desde aqui saludamos").place(x=30, y=50)
etiqueta2 = Label(ventana, text="Desde aquí minimizamos").place(x=30, y=100)
boton1 = Button(ventana, text="Dame click para saludar", command=saludo).place(x=200, y =50)
boton2 = Button(ventana, text="Dame click para minimizar", command=minimizar).place(x=200, y=100)
ventana.mainloop()

#Paso 8 - > Entradas de texto

ventana = Tk()
ventana.title("Entrada de datos")
textbox = Entry(ventana)
textbox.pack()
#ventana.mainloop()

#Paso 9 -> Variables de control: Son objetos especiales que se asocian a los widgets para almacenar sus valores y facilitar su
#disponibilidad en otras partes del programa,
#entero = IntVar()
#flotante = DoubleVar()
#cadena = StringVar()
#boolean = BooleanVar()
#al declarar es posbile asignar un valor inicial
#blog = StringVar(value = "Python para impacientes")
#Método Set para asigar un valor Ej blog.set("Perdón para principiantes")
#Metodo Get para obtener el valor Ej blog.get()

#Ejercicio 2 Saludo Personalizado

def saludar():
    print("Hola: "+nombre.get()+" "+primerApellido.get()+" "+segundoApellido.get())

ventana = Tk()
ventana.title("Entrada de datos")
ventana.geometry("400x400")
nombre = StringVar()
primerApellido = StringVar()
segundoApellido = StringVar()
nombre.set("Escribe tu nombre")
etiqueta1 = Label(ventana, text="Escribe tu nombre: ").place(x=10,y=10)
nombreCaja = Entry(ventana, textvariable = nombre).place(x=170, y=10)
etiqueta2 = Label(ventana, text="Escribe tu primer apellido: ").place(x=10, y=40)
primerApellidoCaja = Entry(ventana, textvariable = primerApellido).place(x=170, y=40)
etiqueta3 = Label(ventana, text="Escribe tu segundo apellido: ").place(x=10,y=70)
segundoApellidoCaja = Entry(ventana, textvariable = segundoApellido).place(x=170, y = 70)
boton= Button (ventana, text = "Saludo Personalizado ", command= saludar).place(x=10, y =100)
ventana.mainloop()





#Ejemplo Botones 1
"""import time

def parpadear():
    ventana.iconify()
    time.sleep(3)
    ventana.deiconify()

ventana = Tk()
boton = Button(ventana, text = "Evento", command=parpadear)
boton.pack()
#ventana.mainloop()"""







#







