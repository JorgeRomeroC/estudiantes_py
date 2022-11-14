import mysql.connector

def Conexion_Db():
    datosConexion = mysql.connector.connect(
        host= "localhost",
        user= "root",
        password= "root",
        port = "8889",
        database = "estudiantes_py"
    )
    return datosConexion

# =====================================
# INSERTAR ALUMNO
#======================================

def registrar(nombre, apellido, carrera, edad):
    midb = Conexion_Db()
    dbCursor = midb.cursor()

    sql = """INSERT INTO alumnos
    (nombre, apellido, carrera, edad)
    VALUES (%s, %s, %s, %s)"""

    valores = (nombre, apellido, carrera, edad)

    try:
        dbCursor.execute(sql, valores)
    except:
        midb.rollback() #rollback: revierte la queri actual y no permite ejecutar la queri nuevamente
        retorno = 1
    else:
        midb.commit() # guardar el registro o los cambio en la db
        retorno = 0
    finally:
        midb.close() # cerrar la conexion
        return retorno

resultado = registrar("Jorge","Romero","Programador", 18)

print(resultado)