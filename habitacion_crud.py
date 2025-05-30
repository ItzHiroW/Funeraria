import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ZeroMoon844",
        database="el_camino"
    )

def insertar_habitacion(capacidad, estado):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO habitacion (capacidad, estado) VALUES (%s, %s)"
    cursor.execute(sql, (capacidad, estado))
    db.commit()
    cursor.close()
    db.close()

def obtener_habitaciones():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM habitacion")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados


def actualizar_habitacion(idhabitacion, estado):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE habitacion SET estado = %s WHERE idhabitacion = %s"
    cursor.execute(sql, (estado, idhabitacion))
    db.commit()
    cursor.close()
    db.close()

def eliminar_habitacion(idhabitacion):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM habitacion WHERE idhabitacion = %s"
    cursor.execute(sql, (idhabitacion,))
    db.commit()
    cursor.close()
    db.close()
