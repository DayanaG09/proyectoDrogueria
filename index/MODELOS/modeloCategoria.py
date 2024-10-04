from index.MODELOS.basededatos import crearConexion

class Categoria:
    def __init__(self):
        self.categoria=None
        self.nombre=None
        
    def getNombre(self):
        return self.nombre
    def setNombre(self,nombre):
        self.nombre=nombre
    
    def crearCategoria(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:   
            cursor.execute("INSERT INTO categoria (Nombre_categoria) VALUES (%s)", (self.nombre,))
            conexion1.commit()
            print("Datos Guardados con exito")
            return True
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
            return False
        finally:   
            cursor.close()
            conexion1.close()         

    #tambien está en el modeloProducto, REVISAR
    def consultarCategoria(self):
        conexion1 = crearConexion()
        cursor = conexion1.cursor()
        try:             
            cursor.execute(f"SELECT * FROM categoria")
            consulta = cursor.fetchall()
            return consulta      
        except Exception as e:
            print(f"Error al consultar la categoria: {e}")    
            return None
        finally:    
            cursor.close()
            conexion1.close()