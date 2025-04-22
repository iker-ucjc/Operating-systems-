import tkinter as tk
from tkinter import ttk
import time
import subprocess
import webbrowser
from itertools import cycle
from PIL import Image, ImageTk

ventanaPrincipal = tk.Tk()
ventanaPrincipal.title("SportOS")
ventanaPrincipal.geometry("1024x600")
ventanaPrincipal.minsize(800, 500)
ventanaPrincipal.maxsize(1920, 1080)
ventanaPrincipal.configure(bg="black")

try:
    icono = ImageTk.PhotoImage(file=r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\SportOS-Logo.ico")
    ventanaPrincipal.iconphoto(False, icono)
except Exception as e:
    print(f"Error al cargar el icono: {e}")

fondo_label = tk.Label(ventanaPrincipal)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

def actualizar_fondo():
    try:
        imagen_fondo = Image.open(r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\FondoPantalla.jpg")
        imagen_fondo = imagen_fondo.resize((ventanaPrincipal.winfo_width(), ventanaPrincipal.winfo_height()), Image.Resampling.LANCZOS)
        fondo_tk = ImageTk.PhotoImage(imagen_fondo)
        fondo_label.config(image=fondo_tk)
        fondo_label.image = fondo_tk
    except Exception as e:
        print(f"Error al cargar el fondo: {e}")

noticias = cycle([
    "🏀 Lakers vencen a Celtics 112-108",
    "⚽ River Plate gana el superclásico 2-1",
    "🎾 Alcaraz avanza a semifinales del Roland Garros",
    "🏈 Chiefs listos para el Super Bowl",
    "🚴‍♂️ Etapa 5 del Tour de Francia en marcha"
])

noticiaActual = tk.StringVar(value=next(noticias))
noticiaLabel = tk.Label(ventanaPrincipal, textvariable=noticiaActual, bg="darkblue", fg="white", font=("Arial", 14), height=2)
noticiaLabel.pack(fill="x", side="top")

def rotarNoticias():
    noticiaActual.set(next(noticias))
    ventanaPrincipal.after(5000, rotarNoticias)

rotarNoticias()

dock = tk.Frame(ventanaPrincipal, bg="#dddddd", width=80)
dock.pack(side="left", fill="y")

apps = {
    "FIFA": {
        "ruta": r"C:\RUTA\A\fifa23.exe",
        "color": "#FF5733",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\FifaLogo.png"
    },
    "Steam": {
        "ruta": r"C:\Program Files (x86)\Steam\Steam.exe",
        "color": "#00FF00",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\SteamLogo.png"
    },
    "YouTube": {
        "ruta": "https://www.youtube.com",
        "color": "#FF0000",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\youtubeLogo.png"
    },
    "Marca": {
        "ruta": "https://www.marca.com/",
        "color": "#0000FF",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\MarcaLogo.png"
    },
    "La Liga": {
        "ruta": "https://www.laliga.com/",
        "color": "#00A4E4",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\LaLigaLogo.png"
    },
    "DAZN": {
        "ruta": "https://www.dazn.com/es-ES/welcome",
        "color": "#1A1A1A",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\DaznLogo.png"
    }
}

iconos_apps = {}

for nombre, info in apps.items():
    ruta = info["ruta"]
    color = info["color"]
    logo_path = info["logo"]

    def abrir_aplicacion(ruta=ruta):
        if ruta.startswith("http"):
            webbrowser.open(ruta)
        else:
            subprocess.Popen([ruta])

    try:
        logo_img = Image.open(logo_path)
        logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)
        logo_tk = ImageTk.PhotoImage(logo_img)
        iconos_apps[nombre] = logo_tk
    except:
        logo_tk = None

    frame_app = tk.Frame(dock, bg="white", padx=5, pady=5)
    frame_app.pack(pady=5)

    def anim_boton(boton):
        def on_enter(e): boton.config(borderwidth=2, highlightthickness=2, highlightbackground="yellow")
        def on_leave(e): boton.config(borderwidth=0, highlightthickness=0)
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

    if logo_tk:
        boton = tk.Button(frame_app, image=logo_tk, bg=color, command=abrir_aplicacion, borderwidth=0)
        boton.image = logo_tk
    else:
        boton = tk.Button(frame_app, text=nombre, bg=color, fg="white", command=abrir_aplicacion)

    anim_boton(boton)
    boton.pack()

    etiqueta = tk.Label(frame_app, text=nombre, bg="white", font=("Arial", 8))
    etiqueta.pack()

# Barra de tareas
barraDeTareas = tk.Frame(ventanaPrincipal, bg="#cccccc", height=50)
barraDeTareas.pack(side="bottom", fill="x")

tk.Button(barraDeTareas, text="Lista de procesos", fg="black", font=("arial", 12),
          command=lambda: subprocess.Popen(["cmd", "/k", "tasklist"])).place(x=10, y=10)

entrada = tk.Entry(barraDeTareas, fg="black", bg="white", font=("arial", 12), width=30)
entrada.insert(0, "Buscar Aplicaciones")
entrada.place(relx=0.5, rely=0.5, anchor="center")

def abrir_por_texto(texto):
    try:
        texto = texto.lower().strip()
        if texto == "bash":
            comando = 'wsl -d Ubuntu bash -c "cd /mnt/c/Users/alfon/Desktop/ProyectosVisualStudio/Universidad/InterfazDeUsuario/ && ./SportOS.sh"'
            subprocess.Popen(comando, shell=True)
        elif texto == "cmd":
            # Abrir CMD de Windows
            subprocess.Popen(["cmd.exe"], shell=True)
        elif texto == "notepad" or texto == "bloc de notas":
            # Abrir Notepad de Windows
            subprocess.Popen(["notepad.exe"], shell=True)
        elif texto.startswith(("http://", "https://")):
            # Abrir URLs en navegador
            webbrowser.open(texto)
        else:
            # Intentar ejecutar otros comandos
            subprocess.Popen([texto], shell=True)
    except FileNotFoundError:
        print(f"Error: No se encontró la aplicación o comando '{texto}'")
    except Exception as e:
        print(f"Error inesperado al ejecutar '{texto}': {e}")
entrada.bind("<Return>", lambda event: abrir_por_texto(entrada.get()))

# Reloj con hover efecto
relojFrame = tk.Frame(barraDeTareas, bg="lightgrey")
relojFrame.place(relx=0.99, rely=0.1, anchor="ne")

etiquetaHora = tk.Label(relojFrame, fg="black", font=("Arial", 12, "bold"), bg="lightgrey")
etiquetaHora.pack()
etiquetaFecha = tk.Label(relojFrame, fg="black", font=("Arial", 10), bg="lightgrey")
etiquetaFecha.pack()

def actualizarHora():
    etiquetaHora.config(text=time.strftime("%H:%M:%S"))
    ventanaPrincipal.after(1000, actualizarHora)

def actualizarFecha():
    etiquetaFecha.config(text=time.strftime("%d/%m/%Y"))
    ventanaPrincipal.after(60000, actualizarFecha)

def hover_reloj(e): relojFrame.config(bg="yellow"); etiquetaHora.config(bg="yellow"); etiquetaFecha.config(bg="yellow")
def leave_reloj(e): relojFrame.config(bg="lightgrey"); etiquetaHora.config(bg="lightgrey"); etiquetaFecha.config(bg="lightgrey")

relojFrame.bind("<Enter>", hover_reloj)
relojFrame.bind("<Leave>", leave_reloj)

actualizarHora()
actualizarFecha()
# ======================================================================
# Iconos directamente en la ventana principal (sin contenedores)
# ======================================================================
iconos_principales = {
    "Bloc de notas": {
        "ruta": "notepad.exe",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\bloq-logo.png",
        "pos_x": 150,
        "pos_y": 100
    },
    "CMD": {
        "ruta": "cmd",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\cmd-logo.png",
        "pos_x": 150,
        "pos_y": 200
    },
    "SportOS Bash": {
        "ruta": "bash",
        "logo": r"C:\Users\alfon\Desktop\ProyectosVisualStudio\Universidad\InterfazDeUsuario\SportOS-Logo.ico",
        "pos_x": 150,
        "pos_y": 300
    }
}

for nombre, info in iconos_principales.items():
    ruta = info["ruta"]
    logo_path = info["logo"]
    pos_x = info["pos_x"]
    pos_y = info["pos_y"]

    def abrir(ruta=ruta):
        abrir_por_texto(ruta)

    try:
        img = Image.open(logo_path)
        img = img.resize((40, 40), Image.Resampling.LANCZOS)
        icono = ImageTk.PhotoImage(img)
    except:
        icono = None

    if icono:
        btn = tk.Button(
            ventanaPrincipal,
            image=icono,
            command=abrir,
            borderwidth=0,
            highlightthickness=0,
            activebackground="black"
        )
        btn.image = icono
        btn.place(x=pos_x, y=pos_y)
        # Efecto hover
        btn.bind("<Enter>", lambda e, b=btn: b.config(highlightbackground="cyan", highlightthickness=2))
        btn.bind("<Leave>", lambda e, b=btn: b.config(highlightthickness=0))
    else:
        btn = tk.Button(
            ventanaPrincipal,
            text=nombre,
            command=abrir,
            fg="black",
            borderwidth=0
        )
        btn.place(x=pos_x, y=pos_y)

    tk.Label(
        ventanaPrincipal,
        text=nombre,
        fg="black",
        font=("Arial", 8)
    ).place(
        x=pos_x + 20,  
        y=pos_y + 45,  
        anchor="center"
    )

actualizar_fondo()
ventanaPrincipal.bind("<Configure>", lambda event: actualizar_fondo())
ventanaPrincipal.mainloop()