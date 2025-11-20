import tkinter as tk
from tkinter import ttk

def inputbox(parent, prompt="Ingrese un valor:", title="InputBox", default_text="") -> dict[str, None]:
    """
    Crea una ventana tipo InputBox usando Toplevel.
    Retorna el texto ingresado o None si se cancela.
    """

    # Ventana hija
    win = tk.Toplevel(parent)
    win.title(title)
    win.resizable(False, False)

    # Hacerla modal
    win.transient(parent)
    win.grab_set()

    # Diccionario para almacenar el resultado
    result = {"value": None}


    # --- Callbacks ---
    def on_ok(event=None):
        result["value"] = entry.get()
        win.destroy()


    def on_cancel(event=None):
        result["value"] = None
        win.destroy()


    win.protocol("WM_DELETE_WINDOW", on_cancel)

    # --- Layout ---
    frm = ttk.Frame(win, padding=10)
    frm.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frm, text=prompt).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 5))

    entry = ttk.Entry(frm, width=40)
    entry.grid(row=1, column=0, columnspan=2, sticky="we", pady=(0, 10))
    entry.insert(0, default_text)

    ttk.Button(frm, text="Aceptar", command=on_ok).grid(row=2, column=0, sticky="e", padx=3)
    ttk.Button(frm, text="Cancelar", command=on_cancel).grid(row=2, column=1, sticky="w", padx=3)

    # Bind Enter y Escape
    win.bind("<Return>", on_ok)
    win.bind("<Escape>", on_cancel)

    # Foco inicial
    entry.focus_set()

    # Centrar la ventana
    win.update_idletasks()
    w, h = win.winfo_width(), win.winfo_height()
    x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (w // 2)
    y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (h // 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

    # Esperar a que la ventana se cierre
    win.wait_window()

    return result["value"]

 