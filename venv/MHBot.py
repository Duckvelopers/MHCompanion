from telegram.ext import Updater, CommandHandler
from venv.config.auth import token

from venv.controller import monsterController as mc
from venv.controller import materialController as mac

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

def bmonstruo(bot, update):
    logger.debug('Busqueda de monstruo recibido')
    mc.busquedaDebug(bot, update)

def bitem(bot, update):
    logger.debug('Busqueda de item recibido')
    mac.busquedaDebug(bot, update)

if __name__ == '__main__':

    logger.info('El bot está iniciado')
    #updater = Updater(token,use_context=True)
    updater = Updater(token=token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('creditos', creditos))
    dispatcher.add_handler(CommandHandler('bitem', bitem))
    dispatcher.add_handler(CommandHandler('bmonstruo', bmonstruo))

    updater.start_polling()
    updater.idle()
