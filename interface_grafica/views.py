# interface_grafica/views.py
import tkinter as tk
from tkinter import messagebox

def calcular_mdc():
    def calcular():
        try:
            a = int(entry_a.get())
            b = int(entry_b.get())
            resultado = maximo_divisor_comum(a, b)
            messagebox.showinfo("Resultado", f"O MDC de {a} e {b} é {resultado}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

    root = tk.Tk()
    root.title("Calculadora de MDC")

    label_a = tk.Label(root, text="Número A:")
    label_a.grid(row=0, column=0, padx=5, pady=5)
    entry_a = tk.Entry(root)
    entry_a.grid(row=0, column=1, padx=5, pady=5)

    label_b = tk.Label(root, text="Número B:")
    label_b.grid(row=1, column=0, padx=5, pady=5)
    entry_b = tk.Entry(root)
    entry_b.grid(row=1, column=1, padx=5, pady=5)

    button_calcular = tk.Button(root, text="Calcular MDC", command=calcular)
    button_calcular.grid(row=2, columnspan=2, padx=5, pady=5)

    root.mainloop()

def maximo_divisor_comum(a, b):
    while b != 0:
        a, b = b, a % b
    return a
