import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk


def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)



class App:
    def __init__(self):
        # self.root = ThemedTk(theme='winxpblue')
        self.root = ThemedTk(theme='arc')

        # textbox
        self.input = tk.StringVar()
        self.edit = ttk.Entry(self.root, textvariable= self.input)
        self.edit.place(relwidth=0.60, relx=0.50, rely=0.35, anchor='center')

        # button
        self.btn = ttk.Button(self.root, text='Calcular factorial', command=self.handler_btn)
        self.btn.place(relwidth=0.60, relx=0.5, rely=0.5, anchor='center')

        # window
        self.root.title('Form1')
        self.root.geometry('500x200')
        self.root.mainloop()

    
    def handler_btn(self) -> None:
        try:
            if self.input.get() != '':
                numero: int = int(self.input.get())
                messagebox.showinfo(parent=self.root, message= factorial(numero), title='Tkinter')

        except ValueError:
            messagebox.showerror(parent=self.root, message='Error de conversion')


def main():
    App()


if __name__ == "__main__":
    main()
