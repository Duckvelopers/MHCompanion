import os
import sqlite3
import json
import logging

db_nombre = r'DDBB\MHCompanion.db'
db_Datos = r'DDBB\Datos'
db_Fotos = r'DDBB\Datos\\'
logger = logging.getLogger('MH_Bot')


def updateMonstruos():
    logger.info('Actualizando Monstruos')
    cont = 0
    with open(db_Datos + r"\Monstruos.json") as json_file:
        data = json.load(json_file)
        try:
            conn = sqlite3.connect(db_nombre)
            cursor = conn.cursor()
            for p in data:
                codigo = p['code']
                archjson = json.dumps(p['json'])
                sqlite_insert = "REPLACE INTO MONSTRUOS(COD_MON, DATOS) VALUES (?, ?)"
                datos_tupla = (codigo, archjson)
                cursor.execute(sqlite_insert, datos_tupla)
                conn.commit()
                cont += 1
                logger.info(codigo+' actualizado')
            cursor.close()
        except sqlite3.Error as error:
            logger.error("Fallo al insertar en la tabla", error)
            return "Error"
        finally:
            if conn:
                conn.close()
                logger.info("Conexion cerrada")
    return str(cont)


def cargarSQL():
    cont = 0
    for file in os.listdir(db_Datos):
        with sqlite3.connect(db_nombre) as conn:
            if file.endswith(".sql"):
                with open(os.path.join(db_Datos, file), 'rt') as f:
                    schema = f.read()
                result = conn.execute(schema)
                for x in result.fetchall():
                    print(x)
                logger.info("Cargado "+file+" con éxito")
                cont += 1
    return str(cont)


def createDDBB():
    if not os.path.exists(db_nombre):
        conn = sqlite3.connect(db_nombre)
        conn.close()
        logger.info('Se ha creado la BBDD')
        return "Se ha creado la BBDD."
    else:
        logger.info('La BBDD ya estaba creada')
        return "La BBDD ya estaba creada"
