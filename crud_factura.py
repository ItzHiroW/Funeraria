from database.conexion import obtener_conexion

def insertar_factura(idfactura, idcliente, idcontrato):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO factura (idfactura, idcliente, idcontrato)
            VALUES (%s, %s, %s)
        """, (idfactura, idcliente, idcontrato))
        conexion.commit()
    conexion.close()

def obtener_facturas():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM factura")
        facturas = cursor.fetchall()
    conexion.close()
    return facturas

def actualizar_factura(idfactura, idcliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE factura SET idcliente = %s WHERE idfactura = %s
        """, (idcliente, idfactura))
        conexion.commit()
    conexion.close()

def eliminar_factura(idfactura):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM factura WHERE idfactura = %s", (idfactura,))
        conexion.commit()
    conexion.close()