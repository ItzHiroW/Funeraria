from database.conexion import obtener_conexion

def insertar_pago(idcontrato, fecha_pago, monto, metodo_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO pagos (idcontrato, fecha_pago, monto, metodo_pago)
            VALUES (%s, %s, %s, %s)
        """, (idcontrato, fecha_pago, monto, metodo_pago))
        conexion.commit()
    conexion.close()

def obtener_pagos():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM pagos")
        pagos = cursor.fetchall()
    conexion.close()
    return pagos

def actualizar_pago(idpago, monto, metodo_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE pagos SET monto = %s, metodo_pago = %s WHERE idpago = %s
        """, (monto, metodo_pago, idpago))
        conexion.commit()
    conexion.close()

def eliminar_pago(idpago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pagos WHERE idpago = %s", (idpago,))
        conexion.commit()
    conexion.close()