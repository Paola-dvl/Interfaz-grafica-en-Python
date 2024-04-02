from tkinter import *
from tkinter import messagebox
import requests

def guardar_cliente():
    nombre = nombre_entry.get()
    correo = correo_entry.get()
    nit = nit_entry.get()

    if not nombre or not correo or not nit:
        messagebox.showerror("Error", "Por favor completa todos los campos.")
        return

    data = {'nombre': nombre, 'correo': correo, 'nit': nit}
    try:
        response = requests.post('http://127.0.0.1:5000/agregarCliente', json=data)
        if response.status_code == 200:
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        else:
            messagebox.showerror("Error", f"No se pudo registrar el cliente: {response.text}")
    except requests.ConnectionError:
        messagebox.showerror("Error", "No se pudo establecer conexión con el servidor.")


root = Tk()
root.title("Registro y visualización de clientes")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 400) // 2
y = (screen_height - 400) // 2

root.geometry(f"400x400+{x}+{y}")

frame_superior = Frame(root)
frame_superior.pack(pady=50)

nombre_label = Label(frame_superior, text="Nombre:")
nombre_label.grid(row=0, column=0, padx=10)

nombre_entry = Entry(frame_superior)
nombre_entry.grid(row=0, column=1, padx=10, pady=20)

correo_label = Label(frame_superior, text="Correo electrónico:")
correo_label.grid(row=1, column=0, padx=10, pady=20)

correo_entry = Entry(frame_superior)
correo_entry.grid(row=1, column=1, padx=10, pady=20)

nit_label = Label(frame_superior, text="NIT:")
nit_label.grid(row=2, column=0, padx=10, pady=20)

nit_entry = Entry(frame_superior)
nit_entry.grid(row=2, column=1, padx=10, pady=20)

guardar_button = Button(root, text="Guardar cliente", command=guardar_cliente)
guardar_button.pack(pady=10)


root.mainloop()