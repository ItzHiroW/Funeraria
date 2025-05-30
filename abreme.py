import os
import subprocess
import sys


if not os.path.exists('funeraria'):
    print("Creando entorno virtual...")
    subprocess.call([sys.executable, "-m", "venv", "funeraria"])


if os.name == 'nt':  # Windows
    activate_script = '.funeraria\Scripts\activate.bat'
else:  # Linux/Mac
    activate_script = '.funeraria/bin/activate'


print("Instalando dependencias...")
subprocess.call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
subprocess.call([sys.executable, "-m", "pip", "install", "-r", "requisitos.txt"])


try:
    from tkcalendar import DateEntry
except ImportError:
    print("tkcalendar no está instalado, instalando...")
    subprocess.call([sys.executable, "-m", "pip", "install", "tkcalendar"])

try:
    import mysql.connector
except ImportError:
    print("mysql-connector-python no está instalado, instalando...")
    subprocess.call([sys.executable, "-m", "pip", "install", "mysql-connector-python"])