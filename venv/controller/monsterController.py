#Clase empleada para búsquedas relacionadas con monstruos

def busquedaDebug(bot, update):
    #logger.info('Debugeando la busqueda de monstruo')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="¡Has buscado un monstruo!"
    )