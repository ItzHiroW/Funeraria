import mysql.connector
from mysql.connector import errorcode
import os

admin_config = {
    'user': 'root',
    'password': 'tu_contraseña_root',
    'host': 'localhost',
    'allow_multi_statements': True 
}

usuario = 'funeraria_user'
clave = 'elcamino'

archivo_sql = 'funeraria.sql'

try:

    cnx = mysql.connector.connect(**admin_config)
    cursor = cnx.cursor()

    with open(archivo_sql, 'r', encoding='utf-8') as f:
        script_sql = f.read()


    for result in cursor.execute(script_sql, multi=True):
        pass 

    print(f"Archivo {archivo_sql} ejecutado correctamente.")

    nombre_db = 'el_camino'

    cursor.execute(f"CREATE USER IF NOT EXISTS '{usuario}'@'localhost' IDENTIFIED BY '{clave}'")
    cursor.execute(f"GRANT ALL PRIVILEGES ON {nombre_db}.* TO '{usuario}'@'localhost'")
    cursor.execute("FLUSH PRIVILEGES")

    print(f"Usuario '{usuario}' creado con permisos sobre la base '{nombre_db}'.")

    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Credenciales incorrectas.")
    else:
        print(f"Error: {err}")

except FileNotFoundError:
    print(f"No se encontró el archivo {archivo_sql}")
