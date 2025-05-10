import tkinter as tk
from tkinter import ttk, messagebox
from conexion import DBConnection
from clientes import Cliente
from servicios import Servicio
from difuntos import Difunto
from cementerios import Cementerio
from contratos import Contrato
from pagos import Pago
from proveedores import Proveedor
from inventario import Inventario

# Configuración de la ventana principal
root = tk.Tk()
root.title('Gestión Funeraria - EL camino')
root.geometry('1400x700')
root.configure(bg='#f5f5f5')

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12))

header_frame = tk.Frame(root, bg='#f5f5f5')
header_frame.grid(row=0, column=0, columnspan=6, sticky='nsew')

ttk.Label(header_frame, text='Sistema Integral de Gestión Funeraria', font=('Helvetica', 18, 'bold')).grid(row=0, column=1, pady=20)

# Menú lateral
menu_frame = tk.Frame(root, bg='#e1e1e1')
menu_frame.grid(row=1, column=0, rowspan=8, sticky='ns')

# Opciones del Menú
options = [
    ('Clientes', Cliente),
    ('Servicios', Servicio),
    ('Difuntos', Difunto),
    ('Cementerios', Cementerio),
    ('Contratos', Contrato),
    ('Pagos', Pago),
    ('Proveedores', Proveedor),
    ('Inventario', Inventario)
]

# Diccionario para instancias
crud_instances = {}

for option, model in options:
    instance = model()
    crud_instances[option] = instance
    ttk.Button(menu_frame, text=option, command=lambda opt=option: actualizar_tabla(opt)).grid(padx=10, pady=5, sticky='ew')

# Frame para los formularios
details_frame = tk.Frame(root, bg='#f5f5f5')
details_frame.grid(row=1, column=5, padx=10, pady=10)

# Tabla de visualización
tree = ttk.Treeview(root, columns=(), show='headings')
tree.grid(row=1, column=1, columnspan=4, pady=20)

# Diccionario para campos
entries = {}

# Método para actualizar la tabla
def actualizar_tabla(nombre_tabla):
    tree.delete(*tree.get_children())
    instancia = crud_instances[nombre_tabla]

    # Definir columnas
    instancia.db.cursor.execute(f"SELECT * FROM {nombre_tabla.lower()} LIMIT 1")
    columnas = [desc[0] for desc in instancia.db.cursor.description]
    tree['columns'] = columnas
    for col in columnas:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    # Obtener registros
    registros = instancia.db.fetch_all(f"SELECT * FROM {nombre_tabla.lower()}")
    for registro in registros:
        tree.insert('', 'end', values=registro)

    # Generar el formulario
    generar_formulario(columnas)

# Método para generar el formulario dinámicamente
def generar_formulario(columnas):
    for widget in details_frame.winfo_children():
        widget.destroy()
    global entries
    entries = {}
    for index, campo in enumerate(columnas):
        label = ttk.Label(details_frame, text=campo)
        label.grid(row=index, column=0, padx=5, pady=5)
        entry = ttk.Entry(details_frame)
        entry.grid(row=index, column=1, padx=5, pady=5)
        entries[campo] = entry

    # Botones CRUD
    ttk.Button(details_frame, text='Guardar', command=guardar_registro).grid(row=len(columnas), column=0, pady=10)
    ttk.Button(details_frame, text='Actualizar', command=actualizar_registro).grid(row=len(columnas), column=1, pady=10)
    ttk.Button(details_frame, text='Eliminar', command=eliminar_registro).grid(row=len(columnas) + 1, column=0, pady=10, columnspan=2)

    # Evento para rellenar el formulario al seleccionar en la tabla
    tree.bind('<ButtonRelease-1>', rellenar_formulario)

# Método para rellenar el formulario
def rellenar_formulario(event):
    selected_item = tree.focus()
    if not selected_item:
        return

    # Obtener los valores del registro seleccionado
    valores = tree.item(selected_item)['values']

    # Rellenar cada campo del formulario
    for index, (campo, entry) in enumerate(entries.items()):
        entry.delete(0, tk.END)
        if index < len(valores):
            entry.insert(0, valores[index])


# ==== CRUD Métodos ====
def guardar_registro():
    datos = [entry.get() for entry in entries.values()]
    instancia = crud_instances[table_name]
    instancia.agregar(*datos)
    actualizar_tabla(table_name)

def actualizar_registro():
    datos = [entry.get() for entry in entries.values()]
    instancia = crud_instances[table_name]
    instancia.actualizar(*datos)
    actualizar_tabla(table_name)

def eliminar_registro():
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning('Advertencia', 'No se ha seleccionado un registro para eliminar')
        return
    confirm = messagebox.askyesno('Confirmación', '¿Estás seguro de que quieres eliminar este registro?')
    if confirm:
        registro_id = entries['id'].get()
        instancia = crud_instances[table_name]
        instancia.eliminar(registro_id)
        actualizar_tabla(table_name)


root.mainloop()