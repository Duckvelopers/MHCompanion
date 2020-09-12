#Clase empleada para búsquedas relacionadas con items

def busquedaDebug(bot, update):
    #logger.info('Debugeando la busqueda de items')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="¡Has buscado un item! ¡Y además acaba de desplegarse la aplicación sola con el commit!"
    )