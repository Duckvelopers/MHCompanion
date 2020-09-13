from telegram.ext import Updater, CommandHandler
#para local usar este import
#from config.auth import token
#para heroku
import os
token = os.environ['HerokuToken']

from controller import monsterController as mc
from controller import materialController as mac

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('MH_Bot')


def start(update, context):
    logger.debug('He recibido un comando start')
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="¡Miáumonos de caza!"
    )


def debug(update, context):
    logger.debug('He recibido un comando debug')
    context.bot.send_message(update.message.chat_id,
        text="Mensaje de Debug htok"
    )


def creditos(update, context):
    logger.info('Recibido comando creditos')
    context.bot.send_message(
        chat_id=update.message.chat_id,
        text="Desarrollado por las mentes de @Kelfindel y @alochimpasplum"
    )


def bmonstruo(update, context):
    logger.debug('Busqueda de monstruo recibido')
    mc.busquedaDebug(update, context)


def bitem(update, context):
    logger.debug('Busqueda de item recibido')
    mac.busquedaDebug(update, context)


if __name__ == '__main__':
    logger.info('El bot está iniciado')
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('debug', debug))
    dispatcher.add_handler(CommandHandler('creditos', creditos))
    dispatcher.add_handler(CommandHandler('bitem', bitem))
    dispatcher.add_handler(CommandHandler('bmonstruo', bmonstruo))

    updater.start_polling()

    updater.idle()
