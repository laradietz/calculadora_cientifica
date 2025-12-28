
import tkinter as tk
import math


def agregar(valor):
    traducciones = {
        "√": "sqrt(",
        "xⁿ": "**",
        "ⁿ√x": "**(1/",
        "eˣ": "e**"
    }
    pantalla.insert(tk.END, traducciones.get(valor, valor))

def limpiar(event=None):
    pantalla.delete(0, tk.END)

def borrar(event=None):
    texto = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, texto[:-1])

def calcular(event=None):
    try:
        expresion = pantalla.get()
        resultado = eval(expresion, {"__builtins__": None}, funciones)
        limpiar()
        pantalla.insert(0, resultado)
    except:
        limpiar()
        pantalla.insert(0, "Error")


funciones = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "sqrt": math.sqrt,
    "log": math.log10,
    "ln": math.log,
    "pi": math.pi,
    "e": math.e
}


ventana = tk.Tk()
ventana.title("Calculadora Científica")
ventana.geometry("360x520")
ventana.resizable(False, False)
ventana.configure(bg="#1e1e1e")


pantalla = tk.Entry(
    ventana,
    font=("Consolas", 22),
    bg="#2b2b2b",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
pantalla.pack(fill="x", padx=15, pady=20, ipady=10)
pantalla.focus_set()


ventana.bind("<Return>", calcular)
ventana.bind("<Escape>", limpiar)
ventana.bind("<BackSpace>", borrar)


frame = tk.Frame(ventana, bg="#1e1e1e")
frame.pack()

def crear_boton(texto, fila, col, color="#413c41"):
    tk.Button(
        frame,
        text=texto,
        width=6,
        height=2,
        font=("Arial", 12),
        bg=color,
        fg="white",
        bd=0,
        activebackground="#605c61",
        command=lambda: (
            calcular() if texto == "=" else
            limpiar() if texto == "C" else
            agregar(texto)
        )
    ).grid(row=fila, column=col, padx=5, pady=5)

# Fila 0
crear_boton("C", 0, 0, "#1cb73b")
crear_boton("(", 0, 1)
crear_boton(")", 0, 2)
crear_boton("√", 0, 3)
crear_boton("/", 0, 4)

# Fila 1
crear_boton("7", 1, 0)
crear_boton("8", 1, 1)
crear_boton("9", 1, 2)
crear_boton("*", 1, 3)
crear_boton("xⁿ", 1, 4)

# Fila 2
crear_boton("4", 2, 0)
crear_boton("5", 2, 1)
crear_boton("6", 2, 2)
crear_boton("-", 2, 3)
crear_boton("ⁿ√x", 2, 4)

# Fila 3
crear_boton("1", 3, 0)
crear_boton("2", 3, 1)
crear_boton("3", 3, 2)
crear_boton("+", 3, 3)
crear_boton("eˣ", 3, 4)

# Fila 4
crear_boton("0", 4, 0)
crear_boton(".", 4, 1)
crear_boton("pi", 4, 2)
crear_boton("e", 4, 3)
crear_boton("=", 4, 4, "#a419d2")

# Fila 5
crear_boton("sin(", 5, 0)
crear_boton("cos(", 5, 1)
crear_boton("tan(", 5, 2)

ventana.mainloop()
