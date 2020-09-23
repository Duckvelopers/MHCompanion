import sqlite3, os, json, logging


db_nombre = os.path.join('DDBB', 'MHCompanion.db')
logger = logging.getLogger('MH_Bot')

def leerMonstruoDDBB(codigo):
    try:
        conn = sqlite3.connect(db_nombre)
        cursor = conn.cursor()
        selQuery = """SELECT DATOS FROM MON_WEAK WHERE COD_MON = ?"""
        cursor.execute(selQuery, (codigo,))
        record = cursor.fetchall()
        for row in record:
            datosJson = row[0]
            datos = json.loads(datosJson)
            logger.info("Leidos datos de: "+datos["name"])
        cursor.close()

    except sqlite3.Error as error:
        logger.error("Failed to read blob data from sqlite table", error)
    finally:
        if conn:
            conn.close()
            logger.debug("sqlite connection is closed")
    return datos
