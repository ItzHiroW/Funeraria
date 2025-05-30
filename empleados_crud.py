import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ZeroMoon844",
        database="el_camino"
    )

def insertar_empleado(nombre, apellido, telefono):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO empleados (nombre, apellido, telefono) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, telefono))
    db.commit()
    cursor.close()
    db.close()

def obtener_empleados():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM empleados")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados


def actualizar_empleado(idempleados, telefono):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE empleados SET telefono = %s WHERE idempleados = %s"
    cursor.execute(sql, (telefono, idempleados))
    db.commit()
    cursor.close()
    db.close()

def eliminar_empleado(idempleados):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM empleados WHERE idempleados = %s"
    cursor.execute(sql, (idempleados,))
    db.commit()
    cursor.close()
    db.close()
