import os
import sqlite3

db_nombreArchivo = r'DDBB\MHCompanion.db'
db_sql = 'DDBB'


def adminDDBB(update, context):
    texto = createdb()
    context.bot.send_message(
        update.message.chat_id,
        text=texto
    )

def cargarSQL(update, context):
    cont = 0
    for file in os.listdir(db_sql):
        with sqlite3.connect(db_nombreArchivo) as conn:
            if file.endswith(".sql"):
                print("Cargando "+file)
                with open(os.path.join(db_sql, file), 'rt') as f:
                    schema = f.read()
                result = conn.execute(schema)
                for x in result.fetchall():
                    print(x)
                print("Cargado "+file+" con éxito")
                cont += 1
    context.bot.send_message(
        update.message.chat_id,
        text="Ficheros cargados: "+str(cont)
    )


def createdb():
    if not os.path.exists(db_nombreArchivo):
        print('Creando BBDD')
        conn = sqlite3.connect(db_nombreArchivo)
        conn.close()
        return "Se ha creado la BBDD."
    else:
        return "La BBDD ya estaba creada"
