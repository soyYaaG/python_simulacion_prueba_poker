import collections
from enum import Enum


class TipoMano(Enum):
    QUINTILLA = 'quintilla'
    POKER = 'poker'
    FULL = 'full'
    TERCIA = 'tercia'
    DOS_PARES = 'dos_pares'
    PAR = 'par'
    TODOS_DIFERENTES = 'todos_diferentes'


class Mano:
    '''
    Clase para retornar el tipo de mano de un número.

    Attributes
    ----------
    `numero: float`
        Número para validar su mano.
    '''
    def __init__(self, numero: float) -> None:
        self._numero: str = f'{numero}'[2:7]


    def obtener(self) -> TipoMano:
        '''
        Retornar el tipo de mano

        `quintilla`: Todos las 5 cartas (números) son iguales.
        `poker`: 4 de las 5 cartas (números) son iguales.
        `full`: 3 (tercia) y 2 (1 par) cartas (números) son iguales.
        `tercia`: 3 de las 5 cartas (números) son iguales.
        `dos_pares`: 2 y 2 de las 5 cartas (números) son iguales.
        `par`: 2 de las 5 cartas (números) son iguales.
        `todos_diferentes`: todas las cartas son diferentes.

        Returns
        -------
        TipoMano
            tipo de mano
        '''
        contador: dict = dict(collections.Counter(self._numero))
        valores_contador = contador.values()

        if 5 in valores_contador:
            return TipoMano.QUINTILLA
        elif 4 in valores_contador:
            return TipoMano.POKER
        elif 3 in valores_contador and 2 in valores_contador:
            return TipoMano.FULL
        elif 3 in valores_contador:
            return TipoMano.TERCIA
        elif 2 in valores_contador:
            contador: int = 0
            for valor in valores_contador:
                if valor == 2:
                    contador += 1

            if contador >= 2:
                return TipoMano.DOS_PARES
            else:
                return TipoMano.PAR
        else:
            return TipoMano.TODOS_DIFERENTES