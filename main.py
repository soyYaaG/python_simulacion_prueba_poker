import os
import random
from prettytable import PrettyTable
from operaciones.mano import Mano
from operaciones.probabilidad import Probabilidad
from operaciones.frecuencia import Frecuencia, DICCIONARIO_BASE


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def header() -> None:
    print('-'*31)
    print('| P R U E B A  D E  P Ó K E R |')
    print('|                             |')
    print('|   Modelación y Simulación   |')
    print('|                             |')
    print('-'*31)


def opciones() -> int:
    print()
    print('1) Generar números pseudoaleatorios y procesar.')
    print('2) Leer archivo con números pseudoaleatorios y procesar.')
    print('3) Salir.')
    print()
    return int(input('Seleccione una opción: '))


def generar_numeros() -> list:
    clear()
    header()
    print()

    try:
        lista_numeros: list = []
        cantidad: int = int(input('Ingrese la cantidad de números a generar: '))
        for _ in range(cantidad):
            lista_numeros.append(random.random())

        return lista_numeros;
    except:
        generar_numeros()


def leer_archivo() -> list:
    clear()
    header()
    print()

    try:
        ruta = input('Ingrese la ruta del archivo: ')
        lista_numeros: list = []

        with open(ruta, 'r') as archivo:
            for valor in archivo.readlines():
                lista_numeros.append(float(valor.strip()))
            archivo.close()

        return lista_numeros;
    except:
        leer_archivo()


def procesar(lista_numeros: list) -> None:
    clear()
    header()
    print()

    tabla: PrettyTable = PrettyTable()
    tabla.align: str = 'l'

    probabilidad: Probabilidad = Probabilidad()
    p: dict = probabilidad.obtener()

    fr_esperada: dict = Frecuencia.frecuencia_esperada(p, len(lista_numeros))
    fr_observada: dict = DICCIONARIO_BASE.copy()
    
    for numero in lista_numeros:
        mano: Mano = Mano(numero)
        fr_observada[mano.obtener().name] += 1;

    fr_observada_2: dict = Frecuencia.frecuencia_observada(fr_esperada, fr_observada)

    tabla.field_names: list = ['Tipo de Mano', 'Fr Observada', 'Fr Esperada', 'Probabilidad']
    for tipo_mano in DICCIONARIO_BASE:
        tabla.add_row([tipo_mano, fr_observada[tipo_mano], fr_esperada[tipo_mano], p[tipo_mano]])


    print(tabla.get_string(sortby='Fr Esperada', reversesort=True))


def run() -> None:
    clear()
    header()

    try:
        opcion: int = opciones()
        
        if opcion == 1:
            procesar(generar_numeros())
        elif opcion == 2:
            procesar(leer_archivo())
        elif opcion == 3:
            clear()
        else:
            run()
    except:
        run()


if __name__ == '__main__':
    run()