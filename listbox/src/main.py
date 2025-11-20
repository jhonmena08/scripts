import tkinter as tk
from tkinter import ttk
from dialog import inputbox


def centrar_ventana(ventana, ancho, alto):
    # Obtener el ancho y alto de la pantalla
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()

    # Calcular la posición x, y 
    x = (ancho_pantalla // 2) - (ancho // 2)
    y = (alto_pantalla // 2) - (alto // 2)

    # Fijar tamaño y ubicación
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
# end


def is_integer(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False
    

def fibonacci(n: int) -> int:
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# end


class App:
    def __init__(self) -> None:

        # ventana principal
        self.root = tk.Tk()

        style = ttk.Style()
        style.configure('MiEstilo.TFrame', background='lightblue')

        # Frame estilo ttk
        self.frame = ttk.Frame(self.root, padding=10, style='MiEstilo.TFrame')
        self.frame.pack(fill="both", expand=True)

        # Etiqueta
        self.label = ttk.Label(self.frame, text= 5*'-' + " Visor " + 5*'-')
        self.label.pack(anchor="w")

        # Scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Listbox
        self.listbox = tk.Listbox(self.frame, height=10, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(fill="both", expand=True)

        # Conectar scrollbar con lisbox
        self.scrollbar.config(command=self.listbox.yview)

        # boton
        self.btn = ttk.Button(self.frame, text='Calcular', command=self.on_click)
        self.btn.pack(side='right', anchor='se', padx=5, pady=5)

        self.root.title("Tkinter")
        centrar_ventana(self.root, 400, 500)
        self.root.mainloop()

    
    def on_click(self) -> None:
        valor = inputbox(self.root, "Ingrese un valor numerico", "Fibonacci", "32")

        if not valor is None and is_integer(valor):
            valor = int(valor)

            self.listbox.delete(0, tk.END)
            for x in range(valor + 1):
                self.listbox.insert(tk.END, f'{x} -> {fibonacci(x)}')

# end class



def main():
    App()


if __name__ == "__main__":
    main()
