import tkinter as tk
import tkinter.messagebox as mb
import random

from conexion import Conexion

fallos=1

def main():
    root = tk.Tk()
    root.title("Ahorcado")
    root.geometry("900x700")
    root.configure(bg="#d7f7f3")
    root.resizable(False, False)

    label = tk.Label(root, text="AHORCADO", font=("Impact", 40), fg="black", bg="#d7f7f3")
    label.place(relx=0.5, rely=0.15, anchor="center")

    botonJugar = tk.Button(root,
                       text="Jugar",
                       font=("Arial", 20),
                       command=lambda: configJugar(root),
                       bg="#007BFF",
                       fg="white",
                       activebackground="#0056b3",
                       activeforeground="white",
                       relief="raised",
                       bd=5,
                       padx=20,
                       pady=10)
    botonJugar.place(relx=0.5, rely=0.5, anchor="center")

    botonUsuarios =  tk.Button(root,
                               text="Ver Victorias y Derrotas de los Usuarios",
                               font=("Arial", 20),
                               command=lambda: buscarUsuarios(root),
                               bg="#007BFF",
                               fg="white",
                               activebackground="#0056b3",
                               activeforeground="white",
                               relief="raised",
                               bd=5,
                               padx=20,
                               pady=10)
    botonUsuarios.place(relx=0.5, rely=0.7, anchor="center")
    root.mainloop()
    usuarios = []


# Ventana de configuracion de la partida
def configJugar(root):
    root.withdraw()

    ventanaCofigJuego = tk.Toplevel(root)
    ventanaCofigJuego.title("Configura tu juego")
    ventanaCofigJuego.geometry("900x700")
    ventanaCofigJuego.configure(bg="#d7f7f3")
    ventanaCofigJuego.resizable(False, False)

    ventanaCofigJuego.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), ventanaCofigJuego.destroy()))

    # Nombre
    nombre = tk.Label(ventanaCofigJuego, text="Introduce tu nombre:", font=("Arial", 16), bg="#d7f7f3")
    nombre.place(relx=0.35, rely=0.15, anchor="center")

    entradaNombre = tk.Entry(ventanaCofigJuego, font=("Arial", 14), bg="#ffffff", fg="black", bd=2, relief="solid")
    entradaNombre.place(relx=0.65, rely=0.15, anchor="center")

    # Variable de la categoria que se va a jugar
    categoria = tk.StringVar()
    categoria.set("frutas")

    textoCategoria = tk.Label(ventanaCofigJuego, text="Selecciona la categoria:", font=("Arial", 16), bg="#d7f7f3")
    textoCategoria.place(relx=0.35, rely=0.3, anchor="center")

    cajaFrutas = tk.Radiobutton(ventanaCofigJuego, text="Frutas", variable=categoria, value = "frutas", bg="#d7f7f3", font=("Arial", 14))
    cajaColores = tk.Radiobutton(ventanaCofigJuego, text="Informatica", variable=categoria, value = "conceptos_informaticos", bg="#d7f7f3", font=("Arial", 14))
    cajaNombres = tk.Radiobutton(ventanaCofigJuego, text="Nombres", variable=categoria, value = "nombres_personas", bg="#d7f7f3", font=("Arial", 14))


    cajaFrutas.place(relx=0.5, rely=0.45, anchor="center")
    cajaColores.place(relx=0.5, rely=0.55, anchor="center")
    cajaNombres.place(relx=0.5, rely=0.65, anchor="center")


    botonEmpezar = tk.Button(ventanaCofigJuego,
                       text="Empezar",
                       font=("Arial", 20),
                       command=lambda: empezarJuego(entradaNombre.get(), categoria.get()),
                       bg="#007BFF",
                       fg="white",
                       activebackground="#0056b3",
                       activeforeground="white",
                       relief="raised",
                       bd=5,
                       padx=20,
                       pady=10)
    botonEmpezar.place(relx=0.5, rely=0.85, anchor="center")

    # Funcion para empezar el juego

    def empezarJuego(nombre, categoria):

        ventanaCofigJuego.withdraw()

        conexion = Conexion()

        # En caso de no haber puesto un nombre o no haber seleccionado una categoria este if te manda de vuelta a la ventana de configuracion
        if not nombre:
            ventanaCofigJuego.deiconify()
            mb.showerror("Error", "Por favor, pon el nombre.")
            return
        else:
            cursor = conexion.obtener_cursor()
            try:
                cursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (nombre,))
                usuario_existente = cursor.fetchone()

                if usuario_existente:
                    # Si el usuario ya existe, mostramos un mensaje
                    mb.showinfo("Usuario existente", f"Se ha seleccionado el usuario {nombre}")
                else:
                    # Si el usuario no existe, insertamos el nuevo usuario en la base de datos
                    cursor.execute("INSERT INTO usuarios (nombre) VALUES (%s)", (nombre,))
                    conexion.conexion.commit()
                    mb.showinfo("Nuevo usuario", f"Se ha creado el usuario {nombre}")
            except Exception as e:
                mb.showerror("Error", f"Ocurrió un error al acceder a la base de datos: {str(e)}")

        ventanaJuego = tk.Toplevel(ventanaCofigJuego)
        ventanaJuego.title("Juego")
        ventanaJuego.geometry("900x700")
        ventanaJuego.configure(bg="#d7f7f3")
        ventanaJuego.resizable(False, False)

        ventanaJuego.protocol("WM_DELETE_WINDOW", lambda: (ventanaCofigJuego.deiconify(), ventanaJuego.destroy()))


        micursor = conexion.obtener_cursor()
        micursor.execute("SELECT * FROM palabras WHERE categoria = %s", (categoria,))
        palabras = []
        palabras = micursor.fetchall()

        # Funcion para actualizar la palabra

        def actualizarPalabra():
            global palabra
            palabra = random.choice(palabras)
            palabraGuionada =  "".join(" _ " if char != " " else "  " for char in palabra[1])
            return palabraGuionada

        foto = tk.PhotoImage(file="Resources/fallo1Ahorcado.png")
        label = tk.Label(ventanaJuego, image=foto, bg="#d7f7f3", bd=1, relief="solid")
        label.place(relx=0.5, rely=0.35, anchor="center")

        textoGuionadoPalabra = tk.Label(ventanaJuego, text=actualizarPalabra(), font=("Arial", 16), bg="#d7f7f3")
        textoGuionadoPalabra.place(relx=0.5, rely=0.7, anchor="center")

        textoNombre = tk.Label(ventanaJuego, text="Jugador: " + nombre, font=("Arial", 16), bg="#d7f7f3")
        textoNombre.place(relx=0.1, rely=0.1, anchor="center")

        insertarLetra = tk.Entry(ventanaJuego, font=("Arial", 16), bg="#d7f7f3")
        insertarLetra.place(relx=0.5, rely=0.8, anchor="center")

        botonVerificar = tk.Button(ventanaJuego,
                                   text="Verificar",
                                   font=("Arial", 16),
                                   command=lambda: verificar(insertarLetra.get(), palabra, textoGuionadoPalabra.cget("text")),
                                   bg="#007BFF",
                                   fg="white",
                                   activebackground="#0056b3",
                                   activeforeground="white",
                                   relief="raised",
                                   bd=5,
                                   padx=20,
                                   pady=10)
        botonVerificar.place(relx=0.5, rely=0.9, anchor="center")

        # Funcion para verificar la letra

        def reiniciarPartida():
            global fallos
            respuesta = mb.askyesno("¿Jugar de nuevo?", "¿Quieres jugar otra partida?")

            if respuesta:
                fallos=0
                textoGuionadoPalabra.config(text=actualizarPalabra())
                foto.config(file=f"Resources/fallo1Ahorcado.png")

            else:
                ventanaCofigJuego.deiconify()
                ventanaJuego.destroy()


        def verificar(letra, palabra, palabraGuionada):
            global fallos
            insertarLetra.delete(0, tk.END)
            palabraAcertar = palabra[1]
            if len(letra) != 1 or letra == " " or not letra.isalpha():
                mb.showerror("Error", "Introduzca solo una letra")
            else:
                letra = letra.lower()
                if letra in palabraAcertar:
                    for char in range(len(palabraAcertar)):
                        if palabraAcertar[char] == letra:
                            palabraGuionada = list(palabraGuionada)
                            palabraGuionada[char*3+1] = letra
                    palabraGuionada = "".join(palabraGuionada)
                    textoGuionadoPalabra.config(text=palabraGuionada)

                    comprobante = "".join(palabraGuionada.split())

                    if comprobante == palabraAcertar:
                        mb.showinfo("¡Felicidades!", "¡Has ganado!")
                        cursor = conexion.obtener_cursor()
                        cursor.execute("UPDATE usuarios SET n_victorias = n_victorias + 1 WHERE nombre = %s", (nombre,))
                        reiniciarPartida()
                        conexion.conexion.commit()
                        cursor.execute("SELECT id FROM usuarios WHERE nombre = %s", (nombre,))
                        idNombre = cursor.fetchone()[0]
                        cursor.execute("INSERT partidas (id_usuario, id_palabra, seGano) VALUES (%s, %s, %s)", (idNombre, palabra[0], True))
                        conexion.conexion.commit()

                else:
                    mb.showerror("Error", f"Letra incorrecta, llevas {fallos} fallos")
                    fallos+=1
                    if fallos <= 6:
                        foto.config(file=f"Resources/fallo{fallos}Ahorcado.png")
                    elif fallos == 7:
                        foto.config(file=f"Resources/fallo{fallos}Ahorcado.png")
                        cursor = conexion.obtener_cursor()
                        cursor.execute("UPDATE usuarios SET n_derrotas = n_derrotas + 1 WHERE nombre = %s", (nombre,))
                        conexion.conexion.commit()
                        mb.showerror("Perdiste", f"Has perdido, la palabra era: {palabraAcertar}")
                        reiniciarPartida()
                        cursor.execute("SELECT id FROM usuarios WHERE nombre = %s", (nombre,))
                        idNombre = cursor.fetchone()[0]
                        cursor.execute("INSERT partidas (id_usuario, id_palabra, seGano) VALUES (%s, %s, %s)", (idNombre, palabra[0], False))
                        conexion.conexion.commit()

        ventanaJuego.mainloop()

    ventanaCofigJuego.mainloop()


# Ventana de Usuarios además de funciones de mostrar, avanzar, retroceder y busqueda
def buscarUsuarios(root):
    root.withdraw()

    global usuarios, indice_actual
    busquedaUsuarios = tk.Toplevel(root)
    busquedaUsuarios.title("Usuarios")
    busquedaUsuarios.geometry("900x700")
    busquedaUsuarios.configure(bg="#d7f7f3")
    busquedaUsuarios.resizable(False, False)

    busquedaUsuarios.protocol("WM_DELETE_WINDOW", lambda: (root.deiconify(), busquedaUsuarios.destroy()))

    conexion = Conexion()
    micursor = conexion.obtener_cursor()
    micursor.execute("SELECT * FROM usuarios")

    usuarios = micursor.fetchall()
    indice_actual = 0

    etiqueta = tk.Label(busquedaUsuarios, text="", font=("Arial", 14), bg="#ffffff", fg="#000000", relief="solid", bd=2, padx=30, pady=30)
    etiqueta.place(relx=0.5, rely=0.5, anchor="center")

    def mostrarUsuario():
        if usuarios:
            usuario = usuarios[indice_actual]
            etiqueta.config(text=f"Usuario: {usuario[0]}\n\nNombre: {usuario[1]}\n\nVictorias: {usuario[2]}\n\nDerrotas: {usuario[3]}")
        else:
            etiqueta.config(text="No hay usuarios.")

    def siguienteUsuario():
        global indice_actual
        if usuarios:
            indice_actual = (indice_actual + 1) % len(usuarios)
            mostrarUsuario()

    def anteriorUsuario():
        global indice_actual
        if usuarios:
            indice_actual = (indice_actual - 1) % len(usuarios)
            mostrarUsuario()

    botonSiguiente = tk.Button(busquedaUsuarios,
                               text="Siguiente",
                               command=siguienteUsuario,
                               bg="#007BFF",
                               fg="white",
                               activebackground="#0056b3",
                               activeforeground="white",
                               relief="raised",
                               bd=5,
                               padx=20,
                               pady=10)

    botonSiguiente.place(relx=0.8, rely=0.5, anchor="center")

    botonAnterior = tk.Button(busquedaUsuarios,
                              text="Anterior",
                              command=anteriorUsuario,
                              bg="#007BFF",
                              fg="white",
                              activebackground="#0056b3",
                              activeforeground="white",
                              relief="raised",
                              bd=5,
                              padx=20,
                              pady=10)
    botonAnterior.place(relx=0.2, rely=0.5, anchor="center")

    mostrarUsuario()

if __name__ == "__main__":
    main()


