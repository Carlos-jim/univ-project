import mysql.connector


class CConexion:
    
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(user="root", password="Carlos69", host="localhost", database = "supermarket", port="3306")
            print(conexion)
            
            
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos {}".format(error))