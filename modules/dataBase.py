from mergeDf import getMergedDf
import mysql.connector
import pandas as pd
from getEnv import getVariable

def getConnexion():
    """
    Hace conexion con la base de datos, las credenciales en .env
    return:
        mySql conexion
    """
    return mysql.connector.connect(
        host=getVariable('host')[0],
        user=getVariable('user')[0],
        passwd=getVariable('passwd')[0]
        )

def executeSchemaScript(cursor):
    """
    Elimina y vuelve a crear el esquema y la tabla vacíos
    args:
       cursor: Cursor de la conexión
    return:
       cursor
    """
    cursor.execute("DROP DATABASE IF EXISTS paises")
    cursor.execute("CREATE SCHEMA IF NOT EXISTS paises DEFAULT CHARACTER SET utf8")
    cursor.execute("USE paises")
    cursor.execute('CREATE TABLE IF NOT EXISTS paises.DatosPaises ('
                   'id INT AUTO_INCREMENT,'
                   'code VARCHAR(3) NOT NULL,'
                   'country VARCHAR(10) NOT NULL,'
                   'population INT(11) NOT NULL,'
                   'year INT(11) NOT NULL,'
                   'ingresos DOUBLE NOT NULL,'
                   'gases DOUBLE NOT NULL,'
                   ' PRIMARY KEY (id));'
                  )
    return cursor

def resetDB():
    """
    Resetea y actualiza datos de la base de datos
    args:
       cursor: Cursor de la conexión
    return:
       cursor
    """
    try:
        df= getMergedDf()
        mydb = getConnexion()
        mycursor = mydb.cursor()
        mycursor=executeSchemaScript(mycursor)
        for _ , row in df.iterrows():
            sql="INSERT INTO DatosPaises (code,country,population,year,ingresos,gases) VALUES ({},{},{},{},{},{})".format("'{}'".format(row['Country Code']), "'{}'".format(row['Country']),row['PopAvg'], row['YEAR'],row['discharges/10**5hab'], row['gas/hab'])
            mycursor.execute(sql)
        mydb.commit()
        del mycursor
        mydb.close()
        print('Base de datos actualizada')
    
    except Exception:
        print('Error Conexion')

resetDB()