import sqlite3
import json
import logging


db_nombre = r'DDBB\MHCompanion.db'
logger = logging.getLogger('MH_Bot')

def leerMonstruoDDBB(codigo):
    try:
        conn = sqlite3.connect(db_nombre)
        cursor = conn.cursor()
        selQuery = """SELECT DATOS FROM MONSTRUOS WHERE COD_MON = ?"""
        cursor.execute(selQuery, (codigo,))
        record = cursor.fetchall()
        for row in record:
            datosJson = row[0]
            datos = json.loads(datosJson)
            logger.info("Leidos datos de: "+datos["nameEsp"])
        cursor.close()

    except sqlite3.Error as error:
        logger.error("Failed to read blob data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            logger.debug("sqlite connection is closed")
    return datos
