import tkinter as tk
from tkinter import ttk


def centrar_ventana(ventana: tk.Tk, ancho: int, alto: int) -> None:
    # calcular la posición x, y 
    x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
    y = (ventana.winfo_screenheight() // 2) - (alto // 2)

    # Fijar tamaño y ubicación
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# end


def init_win_main() -> None:
    counter: int = 0
    
    def on_click() -> None:
        nonlocal counter

        counter += 1
        print(f'Incrementado .. {counter}')
    # end


    root = tk.Tk()

    mybtn = ttk.Button(root, text='Mostrar', command=on_click)
    mybtn.pack(fill='x', expand=True, anchor='center', padx=5)

    root.title('Tkinter')
    centrar_ventana(ventana= root, ancho=300, alto=150)
    root.mainloop()

# end


def main() -> int:
    init_win_main()
    return 0

# end


if __name__ == "__main__":
    main()
