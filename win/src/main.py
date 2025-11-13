import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk


class App:
    def __init__(self):
        self.root = ThemedTk(theme='winxpblue')
        # self.root = ThemedTk(theme='arc')

        self.btn = ttk.Button(self.root, text='Show', command=self.handler_btn)
        self.btn.place(relwidth=0.30, relx=0.5, rely=0.5, anchor='center')

        self.root.title('Form1')
        self.root.geometry('500x200')
        self.root.mainloop()

    
    def handler_btn(self) -> None:
        messagebox.showinfo(parent=self.root, message='Bienvenidos al curso de Python', title='Tkinter')



def main():
    App()


if __name__ == "__main__":
    main()
