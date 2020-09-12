from telegram.ext import Updater, CommandHandler
from config.auth import token

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('MH_Bot')


def start(bot, update):
    logger.info('He recibido un comando start')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="¡Miáumonos de caza!"
    )

def creditos(bot, update):
    logger.info('Recibido comando creditos')
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Desarrollado por las mentes de @Kelfindel y @alochimpasplum"
    )


if __name__ == '__main__':

    logger.info('El bot está iniciado')
    updater = Updater(token,use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('creditos', creditos))

    updater.start_polling()
    updater.idle()
