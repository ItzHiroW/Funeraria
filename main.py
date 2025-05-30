import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

from cliente_crud import insertar_cliente, obtener_clientes, eliminar_cliente
from empleados_crud import insertar_empleado, obtener_empleados, eliminar_empleado
from habitacion_crud import insertar_habitacion, obtener_habitaciones, eliminar_habitacion
from fallecido_crud import insertar_fallecido, obtener_fallecidos, eliminar_fallecido
from funerales_crud import insertar_funeral, obtener_funerales, eliminar_funeral


# Interfaz CRUD de Cliente
def cliente_tab(tab):
    frame_campos = tk.Frame(tab)
    frame_campos.pack(side=tk.LEFT, padx=10, pady=10)

    tk.Label(frame_campos, text="Nombre").pack()
    entry_nombre = tk.Entry(frame_campos)
    entry_nombre.pack()

    tk.Label(frame_campos, text="Apellidos").pack()
    entry_apellidos = tk.Entry(frame_campos)
    entry_apellidos.pack()

    tk.Label(frame_campos, text="Dirección").pack()
    entry_direccion = tk.Entry(frame_campos)
    entry_direccion.pack()

    tk.Label(frame_campos, text="Teléfono").pack()
    entry_telefono = tk.Entry(frame_campos)
    entry_telefono.pack()

    frame_botones = tk.Frame(tab)
    frame_botones.pack(pady=10)

    tabla = ttk.Treeview(tab, columns=("ID", "Nombre", "Apellidos", "Dirección", "Teléfono"), show="headings")
    for col in tabla["columns"]:
        tabla.heading(col, text=col)
    tabla.pack(padx=10, pady=10)

    def agregar():
        nombre = entry_nombre.get()
        apellidos = entry_apellidos.get()
        direccion = entry_direccion.get()
        telefono = entry_telefono.get()
        if nombre and apellidos and direccion and telefono:
            insertar_cliente(nombre, apellidos, direccion, telefono)
            mostrar()
        else:
            messagebox.showwarning("Campos incompletos", "Completa todos los campos")

    def mostrar():
        for fila in tabla.get_children():
            tabla.delete(fila)
        for cliente in obtener_clientes():
            tabla.insert("", tk.END, values=cliente)

    def eliminar():
        seleccionado = tabla.selection()
        if seleccionado:
            id_ = tabla.item(seleccionado[0])["values"][0]
            eliminar_cliente(id_)
            mostrar()

    tk.Button(frame_botones, text="Agregar", command=agregar).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Eliminar", command=eliminar).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Refrescar", command=mostrar).pack(side=tk.LEFT, padx=5)

    mostrar()


# Plantilla general para tabs CRUD
def plantilla_tab(tab, columnas, labels, insertar_func, obtener_func, eliminar_func, widget_por_campo=None):
    frame_campos = tk.Frame(tab)
    frame_campos.pack(side=tk.LEFT, padx=10, pady=10)

    entries = []
    widget_por_campo = widget_por_campo or {}

    for i, label in enumerate(labels):
        tk.Label(frame_campos, text=label).pack()
        if i in widget_por_campo:
            widgets = widget_por_campo[i](frame_campos)
            if isinstance(widgets, (list, tuple)):
                for w in widgets:
                    w.pack()
                entries.append(widgets)
            else:
                widgets.pack()
                entries.append(widgets)
        else:
            entry = tk.Entry(frame_campos)
            entry.pack()
            entries.append(entry)

    frame_botones = tk.Frame(tab)
    frame_botones.pack(pady=10)

    tabla = ttk.Treeview(tab, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col)
    tabla.pack(padx=10, pady=10)

    def agregar():
        valores = []
        for e in entries:
            if isinstance(e, (list, tuple)) and len(e) == 2:
                fecha = e[0].get()
                hora = e[1].get()
                valores.append(f"{fecha} {hora}")
            else:
                valores.append(e.get())

        if all(valores):
            insertar_func(*valores)
            mostrar()
        else:
            messagebox.showwarning("Campos incompletos", "Completa todos los campos")

    def mostrar():
        for fila in tabla.get_children():
            tabla.delete(fila)
        for item in obtener_func():
            tabla.insert("", tk.END, values=item)

    def eliminar():
        seleccionado = tabla.selection()
        if seleccionado:
            id_ = tabla.item(seleccionado[0])["values"][0]
            eliminar_func(id_)
            mostrar()

    tk.Button(frame_botones, text="Agregar", command=agregar).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Eliminar", command=eliminar).pack(side=tk.LEFT, padx=5)
    tk.Button(frame_botones, text="Refrescar", command=mostrar).pack(side=tk.LEFT, padx=5)

    mostrar()


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Funeraria El Camino")
    root.resizable(0,0)
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    tab_cliente = ttk.Frame(notebook)
    tab_empleado = ttk.Frame(notebook)
    tab_habitacion = ttk.Frame(notebook)
    tab_fallecido = ttk.Frame(notebook)
    tab_funeral = ttk.Frame(notebook)

    notebook.add(tab_cliente, text='Clientes')
    notebook.add(tab_empleado, text='Empleados')
    notebook.add(tab_habitacion, text='Habitaciones')
    notebook.add(tab_fallecido, text='Fallecidos')
    notebook.add(tab_funeral, text='Funerales')

    # Clientes
    cliente_tab(tab_cliente)

    # Empleados
    plantilla_tab(
        tab_empleado,
        columnas=["ID", "Nombre", "Apellido", "Teléfono"],
        labels=["Nombre", "Apellido", "Teléfono"],
        insertar_func=insertar_empleado,
        obtener_func=obtener_empleados,
        eliminar_func=eliminar_empleado
    )

    # Habitaciones
    plantilla_tab(
        tab_habitacion,
        columnas=["ID", "Capacidad", "Estado"],
        labels=["Capacidad", "Estado"],
        insertar_func=insertar_habitacion,
        obtener_func=obtener_habitaciones,
        eliminar_func=eliminar_habitacion,
        widget_por_campo={
            1: lambda parent: ttk.Combobox(parent, values=["Disponible", "Ocupada"], state="readonly")
        }
    )

    # Fallecidos (fecha y hora)
    plantilla_tab(
        tab_fallecido,
        columnas=["ID", "Nombre", "Apellido", "Hora", "Causa"],
        labels=["Nombre", "Apellido", "Fecha de Muerte", "Causa de Muerte"],
        insertar_func=insertar_fallecido,
        obtener_func=obtener_fallecidos,
        eliminar_func=eliminar_fallecido,
        widget_por_campo={
            2: lambda parent: [DateEntry(parent, date_pattern="yyyy-MM-dd"), tk.Entry(parent)]
        }
    )

    # Funerales (fecha y hora)
    plantilla_tab(
        tab_funeral,
        columnas=["ID", "Fecha", "Lugar", "ID Fallecido"],
        labels=["Fecha del Funeral", "Lugar", "ID Fallecido"],
        insertar_func=insertar_funeral,
        obtener_func=obtener_funerales,
        eliminar_func=eliminar_funeral,
        widget_por_campo={
            0: lambda parent: [DateEntry(parent, date_pattern="yyyy-MM-dd"), tk.Entry(parent)]
        }
    )

    root.mainloop()
