import mysql.connector

class DBConnection:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ZeroMoon844',
            database='funeraria_el_camino'
        )
        self.cursor = self.conn.cursor()

    def fetch_all(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
