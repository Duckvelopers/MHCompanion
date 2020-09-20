#Clase empleada para búsquedas relacionadas con monstruos
from telegram.ext import Updater, CallbackContext
from DDBB import refMonster as rf


Iconos = '🔥💧⚡❄️️🔱⭐'


def buscarMonstruo(update, context):
    #logger.info('Debugeando la busqueda de monstruo')
    lista = context.args
    if len(lista) < 1:
        mens = "Debes introducir al menos un argumento"
    else:
        mens = buscarNombreMonstruo(lista)
    context.bot.send_message(
        update.message.chat_id,
        text=mens
    )


def buscarNombreMonstruo(args):
    opciones = rf.nombresMonstruo.copy().keys()
    while len(args) > 0:
        busqueda = args.pop(0).lower()
        opciones = [x for x in opciones if x.lower().__contains__(busqueda)]
    if len(opciones) == 1:
        return rf.nombresMonstruo[opciones[0]]
    elif len(opciones) == 0:
        return "Monstruo no encontrado."
    else:
        return rf.nombresMonstruo[min(opciones, key=len)]
