import mysql.connector

class Conexion:
    def __init__(self):
        self.conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="ahorcado",
            port=3306
        )

    def obtener_cursor(self):
        return self.conexion.cursor()
