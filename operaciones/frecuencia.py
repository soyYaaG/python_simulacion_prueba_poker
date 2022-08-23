from unittest import result
from operaciones.mano import TipoMano


DICCIONARIO_BASE = {
    TipoMano.TODOS_DIFERENTES.name: 0,
    TipoMano.PAR.name: 0,
    TipoMano.DOS_PARES.name: 0,
    TipoMano.TERCIA.name: 0,
    TipoMano.FULL.name: 0,
    TipoMano.POKER.name: 0,
    TipoMano.QUINTILLA.name: 0
}


class Frecuencia:
    @staticmethod
    def frecuencia_esperada(probabilidad: dict, tamano: int) -> dict:
        diccionario = DICCIONARIO_BASE.copy()
        for tipo_mano in diccionario.keys():
            diccionario[tipo_mano] = tamano * probabilidad[tipo_mano]

        return diccionario


    @staticmethod
    def frecuencia_observada(fr_esperada: dict, fr_observada: dict) -> float:
        resultado: float = 0

        for tipo_mano in DICCIONARIO_BASE.keys():
            resultado += ((fr_observada[tipo_mano] - fr_esperada[tipo_mano]) ** 2) / fr_esperada[tipo_mano]

        return resultado