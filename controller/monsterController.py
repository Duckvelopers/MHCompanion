#Clase empleada para búsquedas relacionadas con monstruos

def busquedaDebug(update, context):
    #logger.info('Debugeando la busqueda de monstruo')
    context.bot.send_message(
        update.message.chat_id,
        text="¡Has buscado un monstruo!"
    )