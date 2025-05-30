import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="funeraria_user",
        password="elcamino",
        database="el_camino"
    )

def insertar_fallecido(nombre, apellido, hora_muerte, causa_muerte):
    db = conectar()
    cursor = db.cursor()
    sql = "INSERT INTO fallecido (nombre, apellido, hora_muerte, causa_muerte) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nombre, apellido, hora_muerte, causa_muerte))
    db.commit()
    cursor.close()
    db.close()

def obtener_fallecidos():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM fallecido")
    resultados = cursor.fetchall()
    cursor.close()
    db.close()
    return resultados

def actualizar_fallecido(idfallecido, causa_muerte):
    db = conectar()
    cursor = db.cursor()
    sql = "UPDATE fallecido SET causa_muerte = %s WHERE idfallecido = %s"
    cursor.execute(sql, (causa_muerte, idfallecido))
    db.commit()
    cursor.close()
    db.close()

def eliminar_fallecido(idfallecido):
    db = conectar()
    cursor = db.cursor()
    sql = "DELETE FROM fallecido WHERE idfallecido = %s"
    cursor.execute(sql, (idfallecido,))
    db.commit()
    cursor.close()
    db.close()
