import tkinter as tk
from tkinter import ttk

def init() -> None:
    
    def centrar_ventana(ventana, ancho, alto):
        # calcular la posición x, y 
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)

        # Fijar tamaño y ubicación
        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")        


    def on_click() -> None:
        print('Bienvenidos')

        
    root = tk.Tk()

    mybtn = ttk.Button(root, text='Mostrar', command=on_click)
    mybtn.pack(fill='x', expand=True, anchor='center')

    root.title('Tkinter')
    centrar_ventana(root, 300, 150)
    root.mainloop()



def main() -> int:
    init()
    return 0



if __name__ == "__main__":
    main()
