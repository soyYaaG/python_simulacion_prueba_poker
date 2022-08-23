from operaciones import coeficiente_binomial
from operaciones.frecuencia import DICCIONARIO_BASE
from operaciones.mano import TipoMano


class Probabilidad:
    '''
    Clase para calcular la probabilidad de la mano (5 cartas) de un Póker
    '''
    def __init__(self) -> None:
        self._divisor: int = 10**5

    
    def _round(self, value: float) -> float:
        return float(f'{value:.5f}')


    def todos_diferentes(self) -> float:
        '''
        Calcular la probabilidad de sacar todas las carta diferentes.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        return self._round((10*9*8*7*6)/self._divisor)


    def un_par(self) -> float:
        '''
        Calcular la probabilidad de sacar 1 par.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = ((10*9*8*7*1)/self._divisor) * coeficiente_binomial(5, 2)
        return self._round(resultado)


    def dos_pares(self) -> float:
        '''
        Calcular la probabilidad de sacar 2 pares.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = (((10*9*8*1*1)/self._divisor) * coeficiente_binomial(5, 2) * coeficiente_binomial(3, 2)) * (1/2)
        return self._round(resultado)


    def tercia(self) -> float:
        '''
        Calcular la probabilidad de sacar 3 cartas iguales.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = ((10*9*8*1*1)/self._divisor) * coeficiente_binomial(5, 3)
        return self._round(resultado)

    
    def full(self) -> float:
        '''
        Calcular la probabilidad de sacar 3 (tercia) y 2 (par) cartas iguales.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = ((10*9*1*1*1)/self._divisor) * coeficiente_binomial(5, 3) * coeficiente_binomial(2, 2)
        return self._round(resultado)

    
    def poker(self) -> float:
        '''
        Calcular la probabilidad de sacar 4 cartas iguales.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = ((10*9*1*1*1)/self._divisor) * coeficiente_binomial(5, 4)
        return self._round(resultado)


    def quintilla(self) -> float:
        '''
        Calcular la probabilidad de sacar 5 cartas iguales.

        Returns
        -------
        float
            Probabilidad calculada.
        '''
        resultado: float = ((10*1*1*1*1)/self._divisor) * coeficiente_binomial(5, 5)
        return self._round(resultado)


    def obtener(self) -> dict:
        '''
        Devuelve un diccionario con las probabilidades.

        Returns
        -------
        dict
            Diccionario con las probabilidades calculadas.
        '''
        diccionario = DICCIONARIO_BASE.copy()
        
        diccionario[TipoMano.TODOS_DIFERENTES.name] = self.todos_diferentes()
        diccionario[TipoMano.PAR.name] = self.un_par()
        diccionario[TipoMano.DOS_PARES.name] = self.dos_pares()
        diccionario[TipoMano.TERCIA.name] = self.tercia()
        diccionario[TipoMano.FULL.name] = self.full()
        diccionario[TipoMano.POKER.name] = self.poker()
        diccionario[TipoMano.QUINTILLA.name] = self.quintilla()

        return diccionario