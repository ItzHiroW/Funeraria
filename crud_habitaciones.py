from database.conexion import obtener_conexion

def insertar_habitacion(capacidad, estado, idcontrato, idservicio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO habitaciones (capacidad, estado, idcontrato, idservicio)
            VALUES (%s, %s, %s, %s)
        """, (capacidad, estado, idcontrato, idservicio))
        conexion.commit()
    conexion.close()

def obtener_habitaciones():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM habitaciones")
        habitaciones = cursor.fetchall()
    conexion.close()
    return habitaciones

def actualizar_habitacion(idhabitacion, estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE habitaciones SET estado = %s WHERE idhabitacion = %s
        """, (estado, idhabitacion))
        conexion.commit()
    conexion.close()

def eliminar_habitacion(idhabitacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM habitaciones WHERE idhabitacion = %s", (idhabitacion,))
        conexion.commit()
    conexion.close()