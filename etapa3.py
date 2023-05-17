from etapa2 import palabra_sin_tilde, crear_diccionario, mostrar_total_de_palabras
import random

ACENTOS = ("á", "é", "í", "ó", "ú")

def crear_lista_letras(letras):
    '''
    Pre: Recibe una lista cargada previamente con todas las letras del abecedario.
    Post: Genera la lista de 10 letras aleatorias
    '''
    letras_seleccionadas = random.sample(letras, 10)
    letras_seleccionadas.sort()
    return letras_seleccionadas

def filtrar_palabras(palabras, cant_por_letra, letras_seleccionadas):
    """
    Parametros:
        palabras es una lista de palabras que deben estar ordenadas alfabeticamente
        cant_por_letra es una lista de listas en la que el primer valor es la letra y el segundo la cantidad dwe palabras con esa letra en el diccionario
        letras_seleccionadas es una lista de las letras seleccionadas sobre las cuales se deben filtrar las palabras
    """
    CANT = 1
    lista_filtrada = []
    letras_filtradas = []
    index = 0
    for cant in cant_por_letra:
        primer_letra = palabras[index][0] if palabras[index][0] not in ACENTOS else palabra_sin_tilde(palabras[index][0])
        if primer_letra in letras_seleccionadas:
            lista_filtrada.extend(palabras[index:(index+cant[CANT])])
            letras_filtradas.append(cant)
        index += cant[CANT]
    return lista_filtrada, letras_filtradas

def seleccionar_palabra(diccionario_palabras, letras_participantes, cant_por_letra):
    '''
    Pre: Recibe la lista y el diccionario cargados previamente
    Post: Devolverá palabras aleatorias con su definición que empiecen con cada letra de la lista de letras al azar
    '''

    palabras_seleccionadas = []

    claves = sorted(diccionario_palabras.keys(), key=(lambda clave: palabra_sin_tilde(clave[0]) if clave[0] in ACENTOS else clave[0]))
    claves_filtradas, letras_filtradas = filtrar_palabras(claves, cant_por_letra, letras_participantes)
    CANT = 1

    indice = 0
    for cant in letras_filtradas:
        rand = random.randrange(indice, indice+cant[CANT])
        palabra = [claves_filtradas[rand], diccionario_palabras[claves_filtradas[rand]]]
        palabras_seleccionadas.append(palabra)
        indice += cant[CANT]


    palabras_seleccionadas.sort()
    return palabras_seleccionadas




def etapa3_test():
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    diccionario_palabras = crear_diccionario()
    cant_por_letra = mostrar_total_de_palabras(diccionario_palabras)
    cant_por_letra = sorted(cant_por_letra.items(), key = lambda x:x[0])
    

    for i in range(0,500):
        letras_seleccionadas = crear_lista_letras(lista_letras)
        palabras_definiciones = seleccionar_palabra(diccionario_palabras, letras_seleccionadas, cant_por_letra)

        print(letras_seleccionadas)
        for palabra in palabras_definiciones:
            print(palabra[0] + ",", end="")
        print("")

etapa3_test()
