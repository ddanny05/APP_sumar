import tkinter as tk
from tkinter import messagebox
def sumar():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        resultado = num1 + num2
        lbl_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")
# Crear ventana
root = tk.Tk()
root.title("Suma de Dos Números")
root.geometry("300x200")
# Etiquetas y campos de entrada
tk.Label(root, text="Número 1:").pack(pady=5)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text="Número 2:").pack(pady=5)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Botón de sumar
btn_sumar = tk.Button(root, text="Sumar", command=sumar)
btn_sumar.pack(pady=10)

# Etiqueta para mostrar el resultado
lbl_resultado = tk.Label(root, text="Resultado: ")
lbl_resultado.pack(pady=10)

# Ejecutar ventana
root.mainloop()
