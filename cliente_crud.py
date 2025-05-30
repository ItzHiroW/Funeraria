import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="funeraria_user",
        password="elcamino",
        database="el_camino"
    )

def insertar_cliente(nombre, apellidos, direccion, telefono):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO cliente (nombre, apellidos, direccion, telefono) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, apellidos, direccion, telefono))
    db.commit()
    cursor.close()
    db.close()

def obtener_clientes():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM cliente")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados

def actualizar_cliente(idcliente, telefono):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE cliente SET telefono = %s WHERE idcliente = %s"
    cursor.execute(sql, (telefono, idcliente))
    db.commit()
    cursor.close()
    db.close()

def eliminar_cliente(idcliente):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM cliente WHERE idcliente = %s"
    cursor.execute(sql, (idcliente,))
    db.commit()
    cursor.close()
    db.close()
9
