from telegram.ext import Updater, CommandHandler
from controller import monsterController as mc
from controller import materialController as mac
from controller import apiRest as ar
from DDBB import dbAdmin as dba

import logging
#para local usar este import
from config.auth import token
#para heroku
#import os
#token = os.environ['HerokuToken']

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('MH_Bot')


def start(update, context):
    logger.debug('Recibido comando start')
    ar.handleCommand("start")
    context.bot.send_message(
        update.message.chat_id,
        text="¡Miáumonos de caza!"
    )


def debug(update, context):
    logger.debug('Recibido comando debug')
    ar.handleCommand("debug")
    context.bot.send_message(
        update.message.chat_id,
        text="Mensaje de Debug ⭐🔥💧❄⚡️️🔱♆❌"
    )


def creditos(update, context):
    logger.info('Recibido comando creditos')
    ar.handleCommand("creditos")
    context.bot.send_message(
        update.message.chat_id,
        text="Desarrollado por las mentes de @Kelfindel y @alochimpasplum"
    )


def bmonstruo(update, context):
    logger.debug('Busqueda de monstruo recibido')
    ar.handleCommand("bmonstruo")
    mc.buscarMonstruo(update, context)


def bitem(update, context):
    logger.debug('Busqueda de item recibido')
    ar.handleCommand("bitem")
    mac.busquedaDebug(update, context)


def dbCrear(update, context):
    ar.handleCommand("dbAdmin")
    texto = dba.createDDBB()
    context.bot.send_message(
        update.message.chat_id,
        text=texto
    )


def dbCargarSql(update, context):
    ar.handleCommand("dbCarga")
    texto = dba.cargarSQL()
    context.bot.send_message(
        update.message.chat_id,
        text="Ficheros cargados: "+texto
    )


def dbUpdateMons(update, context):
    ar.handleCommand("dbUpdateMons")
    texto = dba.updateMonstruos()
    context.bot.send_message(
        update.message.chat_id,
        text="Cargados "+texto+" monstruos."
    )


if __name__ == '__main__':
    logger.info('El bot está iniciado')
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('debug', debug))
    dispatcher.add_handler(CommandHandler('creditos', creditos))
    dispatcher.add_handler(CommandHandler('bitem', bitem))
    dispatcher.add_handler(CommandHandler('bmons', bmonstruo))
    dispatcher.add_handler(CommandHandler('dbCrear', dbCrear))
    dispatcher.add_handler(CommandHandler('dbCargarSql', dbCargarSql))
    dispatcher.add_handler(CommandHandler('dbUpdateMons', dbUpdateMons))

    lista = (
        ("start", "Bienvenida"),
        ("debug", "Comando de prueba"),
        ("creditos", "Info de mis creadores"),
        ("bitem", "Para buscar item, Usar \\bitem objetoABuscar"),
        ("bmons", "Para buscar item, Usar \\bmons Nombre Sub")
    )
    dispatcher.bot.set_my_commands(lista)

    updater.start_polling()

    updater.idle()
