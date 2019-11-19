from mergeDf import getMergedDf
import mysql.connector
import pandas as pd

def executeSchemaScript(cursor):
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
    try:
        df= getMergedDf()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
        )
        mycursor = mydb.cursor()
        mycursor=executeSchemaScript(mycursor)
        for index, row in df.iterrows():
            sql="INSERT INTO DatosPaises (code,country,population,year,ingresos,gases) VALUES ({},{},{},{},{},{})".format("'{}'".format(row['Country Code']), "'{}'".format(row['Country']),row['PopAvg'], row['YEAR'],row['discharges/10**5hab'], row['gas/hab'])
            mycursor.execute(sql)
        mydb.commit()
        del mycursor
        mydb.close()
        return 'Base de datos actualizada'
    
    except Exception:
        return 'Error Conexion'
