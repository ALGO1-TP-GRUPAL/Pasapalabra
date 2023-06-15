from tkinter import *
from tkinter import messagebox
import csv
import random

MAX_REGISTRO = [0, 9999999]

def crear_root():
    '''
    Función: crear_root
    Parámetros: -
    Salida: Devuelve el root necesario para la interfaz.
    '''

    global root
    root = Tk()

    root.title('Pasapalabra')
    root.resizable(0, 0)
    root.geometry('650x350')
    root.iconbitmap('words.ico')
    root.config(bg= '#778899')

    return root

def crear_frame(root):
    '''
    Función: crear_frame
    Parámetros: root es la raiz configurada previamente
    Salida: Devolverá el frame con el que se trabajará a futuro
    '''

    frame_1 = Frame(root, width = 500, height = 450)
    frame_1.config(bg = '#2F4F4F')
    frame_1.pack()

    return frame_1


def mensaje_de_inicio(root, frame):
    '''
    Función: mensaje_de_inicio
    Parámetros: root es la raiz configurada previamente
                frame_1 frame configurado previamente
    Salida: Muestra el mensaje para empezar el juego con los botones iniciar y salir
    '''
    
    texto_1 = Label(frame, text = 'Pasapalabra!')
    texto_1.config(bg = '#2F4F4F', font = ('Hack', 40))
    texto_1.place(x = 100, y = 80)

    boton_inicio = Button(frame, text = 'Jugar', font = ('Comic Sans', 15), command = lambda : inicio(root, frame), bg= '#778899')
    boton_inicio.place(x = 120, y = 220, width = 100, height = 50)

    boton_salir = Button(frame, text = 'Salir', font = ('Comic Sans', 15), command = root.destroy, bg= '#778899')
    boton_salir.place(x = 250, y = 220, width = 100, height = 50)
    #boton_inicio.pack() O uso .place o uso pack() con los grids

def inicio(root, frame):
    '''
    Función: inicio
    Parámetros: root y frame creados previamente
    Salida: Destruye la ventana con el mensaje inicial y pasa al login de usuarios
    '''

    frame.destroy()
    login_usuarios(root, frame)

def login_usuarios(root, frame):
    '''
    Función: login_usuarios
    Parámetros: root y frame creados previamente
    Salida: Mostrar la ventana para acceder un usuario o crear en caso de que no exista
    '''

    global caja_usuario
    global caja_clave
    
    frame_usuarios = Frame(width = 400, height = 350)
    frame_usuarios.config(bg = '#2F4F4F')
    frame_usuarios.pack()

    texto_login = Label(frame_usuarios, text = 'Ingresar información')
    texto_login.config(bg = '#2F4F4F', font = ('Hack', 20))
    texto_login.place(x = 70, y = 60)

    label_usuario = Label(frame_usuarios, text = 'Usuario: ', bg = '#778899', fg = "black", justify = "left", font = 15)
    label_usuario.place(x = 70, y = 130, width = 90, height = 30)
    caja_usuario = Entry(frame_usuarios, bg = "#778899", fg = "black", justify = "left", font = 15)
    caja_usuario.place(x = 180, y = 130, width = 150, height = 30)

    label_clave = Label(frame_usuarios, text = 'Clave: ', bg = '#778899', fg = "black", justify = "left", font = 15)
    label_clave.place(x = 70, y = 180, width = 90, height = 30)
    caja_clave = Entry(frame_usuarios, bg = "#778899", fg = "black", justify = "left", font = 15)
    caja_clave.place(x = 180, y = 180, width = 150, height = 30)
    caja_clave.config(show = '*')

    boton_de_registro = Button(frame_usuarios, text = 'Registrarse', font = ('Comic Sans', 10), command = registro_nuevo, bg = '#778899')
    boton_de_registro.place(x = 90, y = 250, width = 100, height = 30)

    boton_ingreso = Button(frame_usuarios, text = 'Ingresar', command = lambda : validar_ingreso(root), font = ('Comic Sans', 10), bg = '#778899')
    boton_ingreso.place(x = 200, y = 250, width = 100, height = 30)

    boton_iniciar_partida = Button(frame_usuarios, text = 'Iniciar partida', font = ('Comic Sans', 10), command = obtener_lista_jugadores, bg = '#778899')
    boton_iniciar_partida.place(x = 90, y = 285, width = 100, height = 30)

    boton_salir = Button(frame_usuarios, text = 'Salir', font = ('Comic Sans', 10), command = root.destroy, bg = '#778899')
    boton_salir.place(x = 200, y = 285, width = 100, height = 30)

def registro_nuevo():
    '''
    Función: registro_nuevo
    Parámetros: -
    Salida: Crear un nuevo usuario con una nueva clave con sus validaciones respectivas
    '''

    global registro_usuario
    global caja_texto_usuario
    global caja_texto_clave
    global confirmacion_caja_nueva

    registro_usuario = Tk()
    registro_usuario.title('Crear nuevo usuario')
    registro_usuario.resizable(0, 0)
    registro_usuario.geometry('300x300')
    registro_usuario.config(bg = '#206f8b')
    registro_usuario.iconbitmap('login.ico')

    usuario = StringVar()
    clave = StringVar()
    reconfirmar_clave = StringVar()

    usuario_nuevo = Label(registro_usuario, text = 'Nuevo usuario:', bg = '#206f8b', fg = "black", justify = "left", font = 5)
    usuario_nuevo.place(x = 50, y = 10)
    caja_texto_usuario = Entry(registro_usuario, textvariable = usuario, bg = "#2F4F4F", fg = "white", justify = "left", font = 5)
    caja_texto_usuario.place(x = 50, y = 40, width = 200, height = 30)

    clave_nueva = Label(registro_usuario, text = 'Nueva clave:', bg = '#206f8b', fg = "black", justify = "left", font = 5)
    clave_nueva.place(x = 50, y = 70)
    caja_texto_clave = Entry(registro_usuario, textvariable = clave, bg = "#2F4F4F", fg = "white", justify = "left", font = 5)
    caja_texto_clave.place(x = 50, y = 100, width = 200, height = 30)

    confirmacion_nueva = Label(registro_usuario, text = 'Confirmar clave:', bg = '#206f8b',fg = "black", justify = "left", font = 5)
    confirmacion_nueva.place(x = 50, y = 130)
    confirmacion_caja_nueva = Entry(registro_usuario, textvariable = reconfirmar_clave, bg = "#2F4F4F", fg = "white", justify = "left", font = 5)
    confirmacion_caja_nueva.place(x = 50, y = 160, width = 200, height = 30)

    boton_confirmar = Button(registro_usuario, text = 'Confirmar', font = ('Comic Sans', 10), command = verificar_datos, bg = '#2F4F4F')
    boton_confirmar.place(x = 50, y = 200, width = 100, height = 30)

    boton_cancelar = Button(registro_usuario, text = 'Cancelar', font = ('Comic Sans', 10), command = registro_usuario.destroy, bg = '#2F4F4F')
    boton_cancelar.place(x = 160, y = 200, width = 100, height = 30)

    

def verificar_datos():
    '''
    Función: verificar_datos
    Parámetros: -
    Salida: Si los datos ingresados tienen un error devolverá un mensaje de advertencia caso contrario que se ha creado con éxito el usuario
    '''

    archivo_usuarios = open('usuarios.csv', 'a+', newline = '')
    writer = csv.writer(archivo_usuarios, delimiter = ',')
    
    usuario_1 = caja_texto_usuario.get()
    clave_1 = caja_texto_clave.get()
    clave_2 = confirmacion_caja_nueva.get()
    usuario_valido = False
    clave_valida = False

    mayusc = 0
    minusc = 0
    letras = 0
    numeros = 0
    guion_medio = 0
    caracteres_especiales = 0
    acentos = 0

    letras_acentuadas = ['á', 'í', 'ú', 'ó', 'é']
    
    if 4 <= len(usuario_1) <= 20:
        for caracter in usuario_1:
            if caracter.isalpha():
                letras += 1
            if caracter.isnumeric():
                numeros += 1
            if caracter == '-':
                guion_medio += 1

    if 6 <= len(clave_1) <= 12:
        for caracter in clave_1:
            if caracter.isupper():
                mayusc += 1
            if caracter.islower():
                minusc += 1
            if caracter.isnumeric():
                numeros += 1
            if caracter == '#' or caracter == '!':
                caracteres_especiales += 1
            if caracter in letras_acentuadas:
                acentos += 1

    if mayusc > 0 and minusc > 0 and numeros > 0 and caracteres_especiales > 0 and acentos == 0:
        clave_valida = True

    if clave_1 != clave_2:
        clave_valida = False
        Label(registro_usuario, bg = '#206f8b', text = 'No coinciden las claves', font = ('Times', 14)).place(x = 50, y = 235)
        
    if letras > 0 and numeros > 0 and guion_medio > 0:
        usuario_valido = True

    if usuario_valido and clave_valida:
        archivo_usuarios.seek(0)
        usuarios_creados = [fila.split(',')[0] for fila in archivo_usuarios]
        if usuario_1 in usuarios_creados:
            messagebox.showinfo('Aviso', 'El usuario ya existe')
            
        else:
            writer.writerow([usuario_1, clave_1])
            Label(registro_usuario, bg = '#206f8b', text = 'Creación exitosa', font= ('Times', 20)).place(x = 50, y = 235)
            caja_texto_usuario.delete(0, END)
            caja_texto_clave.delete(0, END)
            confirmacion_caja_nueva.delete(0, END)

    else:
        messagebox.showwarning('Error', 'Revisar los datos')

    archivo_usuarios.close()


def obtener_linea(archivo_usuarios):

    linea = archivo_usuarios.readline()
    registro = []

    if linea:
        registro = linea.rstrip('\n').split(',')

    else:
        registro = MAX_REGISTRO

    return registro

def validar_ingreso(root):
    '''
    Función: validar_ingreso
    Parámetros: root es recibido para poder eliminarlo cuando se valide el ingreso
    Salida:
    '''

    global lista_jugadores

    archivo_usuarios = open('usuarios.csv', 'r')
    linea = obtener_linea(archivo_usuarios)
    nombre_string = caja_usuario.get()
    clave_string = caja_clave.get()
    usuario, clave = linea
    valido = False
    lista_jugadores = []

    while usuario and valido == False: 

        if nombre_string == usuario and clave_string == clave:
            lista_jugadores.append([usuario, clave])
            messagebox.showinfo('Acceso', 'Usuario válido')
            caja_usuario.delete(0, END)
            caja_clave.delete(0, END)
            valido = True
        
        linea = obtener_linea(archivo_usuarios)
        usuario, clave = linea
    

    if not valido:
        messagebox.showwarning('Incorrecto', 'Usuario inválido')

def obtener_lista_jugadores():
    '''
    Función: obtener_lista_jugadores
    Parámetros: -
    Salida: Devuelve la lista con los jugadores ordenados aleatoriamente para poder empezar el juego
    '''

    jugadores = lista_jugadores.get()
    random.shuffle(jugadores)

    return print(jugadores)

def main():
    
    root = crear_root()
    frame = crear_frame(root)

    mensaje_de_inicio(root, frame)
    root.mainloop()

main()