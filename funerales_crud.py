import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="funeraria_user",
        password="elcamino",
        database="el_camino"
    )

def insertar_funeral(fecha_funeral, lugar, fallecido_id):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO funerales (fecha_funeral, lugar, fallecido_idfallecido) VALUES (%s, %s, %s)"
    cursor.execute(sql, (fecha_funeral, lugar, fallecido_id))
    db.commit()
    cursor.close()
    db.close()

def obtener_funerales():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM funerales")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados

def actualizar_funeral(idfunerales, lugar):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE funerales SET lugar = %s WHERE idfunerales = %s"
    cursor.execute(sql, (lugar, idfunerales))
    db.commit()
    cursor.close()
    db.close()

def eliminar_funeral(idfunerales):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM funerales WHERE idfunerales = %s"
    cursor.execute(sql, (idfunerales,))
    db.commit()
    cursor.close()
    db.close()
