#Clase empleada para búsquedas relacionadas con monstruos
from DDBB import refMonster as rf
from DDBB import dbController as dbC

import logging

logger = logging.getLogger('MH_Bot')
Iconos = '⭐🔥💧❄⚡️️🔱❌'


def buscarMonstruo(lista):
    if len(lista) < 1:
        return "Debes introducir al menos un argumento"
    else:
        return detallesMonstruo(buscarNombreMonstruo(lista))


def buscarNombreMonstruo(args):
    opciones = rf.nombresMonstruo.copy().keys()
    while len(args) > 0:
        busqueda = args.pop(0).lower()
        opciones = [x for x in opciones if x.lower().__contains__(busqueda)]
    if len(opciones) == 1:
        return rf.nombresMonstruo[opciones[0]]
    elif len(opciones) == 0:
        return None
    else:
        return rf.nombresMonstruo[min(opciones, key=len)]


#UPDATEAR CON ESTRUCTURA BBDD
def detallesMonstruo(codigo):
    logger.info('Codigo recibido: '+codigo)
    if codigo is None:
        return "Monstruo no encontrado."
    else:
        datos = dbC.leerMonstruoDDBB(codigo)
        texto = "Nombre del Monstruo: {}\n🔥: {}\n💧: {}\n⚡: {}\n❄️️: {}\n🔱: {}".format(
            datos["name"],
            estrellas(datos["fire"]),
            estrellas(datos["water"]),
            estrellas(datos["thunder"]),
            estrellas(datos["ice"]),
            estrellas(datos["dragon"]))
        print(texto)
        return texto


def estrellas(int):
    if int == 0:
        return "❌"
    else:
        return int*'⭐'