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

#resultado = registrar("Zoe","Romero","Diseñador grafico", 20)

#print(resultado)

# =====================================
# LISTAR ALUMNOS
#======================================

def listar():
    midb = Conexion_Db()
    dbCursor = midb.cursor()

    sql = """SELECT * FROM alumnos"""
    #sql = """SELECT * FROM alumnos WHERE id = 1"""

    try:
        dbCursor.execute(sql)
    except:
        midb.rollback()
        retorno = 1
    else:
        retorno = []
        for alumno in dbCursor:
            retorno.append(alumno)
    finally:
        midb.close()
        return retorno

#resultado = listar()
#print(resultado)


# =====================================
# LISTAR SOLO ALUMNOS POR ID
#======================================

def Listar_Por_Id(id):
    midb = Conexion_Db()
    dbCursor = midb.cursor()

    sql = """SELECT * FROM alumnos WHERE id = %s"""

    valores = (id,)

    try:
        dbCursor.execute(sql, valores)
    except:
        midb.rollback()
        retorno = 1
    else:
        retorno = ()
        for alumno in dbCursor:
            retorno = alumno
    finally:
        midb.close()
        return retorno

#resultado = Listar_Por_Id(2)
#print(resultado)

# =====================================
# ACTUALIZAR ALUMNO
#======================================

def actualizar_carrera(carrera, id):
    midb = Conexion_Db()
    dbCursor = midb.cursor()

    sql = """UPDATE alumnos SET carrera = %s WHERE id = %s"""

    valores = (carrera, id)

    try:
        dbCursor.execute(sql, valores)
    except:
        midb.rollback()
        retorno = 1
    else:
        midb.commit()
        retorno = 0
    finally:
        midb.close()
        return retorno

#resultado = actualizar_carrera('Ingenieria Informatica', 1)
#print(resultado)

# =====================================
# ELIMINAR ALUMNO
#======================================

def eliminar(id):
    midb = Conexion_Db()
    dbCursor = midb.cursor()

    sql = """DELETE FROM alumnos WHERE id = %s"""

    valores = (id,)

    try:
        dbCursor.execute(sql, valores)
    except:
        midb.rollback()
        retorno = 1
    else:
        midb.commit()
        retorno = 0
    finally:
        midb.close()
        return retorno

#resultado = eliminar(1)
#print(resultado)