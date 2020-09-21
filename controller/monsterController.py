#Clase empleada para búsquedas relacionadas con monstruos
from DDBB import refMonster as rf
from DDBB import dbController as dbC


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
        return detallesMonstruo(rf.nombresMonstruo[opciones[0]])
    elif len(opciones) == 0:
        return "Monstruo no encontrado."
    else:
        return detallesMonstruo(rf.nombresMonstruo[min(opciones, key=len)])


def detallesMonstruo(codigo):
    datos = dbC.leerMonstruoDDBB(codigo)
    if datos is str:
        return datos
    else:
        texto = "Nombre del Monstruo: {}\nDeb.fuego: {}\nDeb.Agua: {}\nDeb.Electro: {}\nDeb.Hielo: {}\nDeb.Dragon: {}\nRompibles: {}".format(
            datos["nameEsp"],
            (datos["fireWeak"]*'⭐'),
            (datos["waterWeak"]*'⭐'),
            (datos["electricWeak"]*'⭐'),
            (datos["iceWeak"]*'⭐'),
            (datos["dragonWeak"]*'⭐'),
            datos["breakEsp"])
        print(texto)
        return texto
