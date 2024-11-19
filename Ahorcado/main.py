import tkinter as tk
import tkinter.messagebox as mb

from conexion import Conexion

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
    categoria.set(None)

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

        # En caso de no haber puesto un nombre o no haber seleccionado una categoria este if te manda de vuelta a la ventana de configuracion

        if not nombre or not categoria:
            ventanaCofigJuego.deiconify()
            mb.showerror("Error", "Por favor, introduce tu nombre y selecciona una categoría.")
            return

        ventanaJuego = tk.Toplevel(ventanaCofigJuego)
        ventanaJuego.title("Juego")
        ventanaJuego.geometry("900x700")
        ventanaJuego.configure(bg="#d7f7f3")
        ventanaJuego.resizable(False, False)

        ventanaJuego.protocol("WM_DELETE_WINDOW", lambda: (ventanaCofigJuego.deiconify(), ventanaJuego.destroy()))



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

    botonSiguiente.place(relx=0.2, rely=0.5, anchor="center")

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
    botonAnterior.place(relx=0.8, rely=0.5, anchor="center")

    mostrarUsuario()


if __name__ == "__main__":
    main()


