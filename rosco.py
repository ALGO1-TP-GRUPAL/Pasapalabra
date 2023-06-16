from palabras_y_definiciones import quitar_acentos
import random

ACENTOS = ("á", "é", "í", "ó", "ú")

def obtener_letras_particip(CANT_LETRAS):
    '''
    Función: obtener_letras_particip
    Parámetros: 
        - CANT_LETRAS: Es un integer constante que representa cuántas letras conformarán el rosco. Éste valor se obtiene de configuracion
    Salida: 
        - letras_particip: Es una lista de una selección aleatoria de letras del abecedario del largo indicado por parámetro
    Precondiciones: Se debe haber leido correctamente las configuraciones el juego y haber iniciado una partida nueva
    Postcondiciones: Crea una lista con las letras participantes del rosco
    Autores: Valentín Marturet / Renato Villalba / Valentina Llanos Pontaut
    '''
    LETRAS = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letras_particip = random.sample(LETRAS, CANT_LETRAS)
    letras_particip.sort()    
    return letras_particip

def filtrar_palabras(palabras, cant_por_letra, letras_seleccionadas):
    '''
    Función: filtrar_palabras
    Parametros: 
        - palabras: Es una lista de palabras que deben estar ordenadas alfabeticamente.
        - cant_por_letra: Es una lista de listas en la que el primer valor es la letra y el segundo la cantidad de palabras con esa letra en el diccionario.
        - letras_seleccionadas: Es una lista de las letras seleccionadas sobre las cuales se deben filtrar las palabras.
    Salida: 
        - lista_filtrada: es una lista de palabras que sólo comienzan con alguna de las letras participantes seleccionadas de forma aleatoria anteriormente
    Precondiciones: Se deben haber seleccionado las letras participantes, haber leído correctamente las configuraciones del juego y haber iniciado una partida nueva
    Postcondiciones: Se obtienen todas las posibles palabras que pueden ser seleccionadas para participar en el rosco ya sabiendo qué letras son las participantes
    Autores: Valentín Marturet / Renato Villalba / Valentina Llanos Pontaut
    '''
    CANT = 1
    lista_filtrada = []
    index = 0
    for letra_cant in cant_por_letra:
        primer_letra = palabras[index][0] if palabras[index][0] not in ACENTOS else quitar_acentos(palabras[index][0])
        if primer_letra in letras_seleccionadas:
            lista_filtrada.extend(palabras[index:(index+letra_cant[CANT])])
        index += letra_cant[CANT]
    return lista_filtrada

def obtener_palabrasydefiniciones_particip(diccionario_palabras_definicion, letras_participantes, palabras_por_letra):
    '''
    Función: obtener_palabrasydefiniciones_particip
    Parámetros: 
        - diccionario_palabras: Diccionario cargado con las palabras como claves y sus difiniciones como valores.
        - letras_participantes: Lista de 10 letras aleatorias.
        - cant_por_letra: Lista que contiene sublistas con cada letra del abecedario y la cantidad de palabras que comiencen con esa letra.
    Salida: 
        - palabrasydefiniciones_seleccionadas = es una lista de listas cuyas sublistas contienen las palabras y definiciones participantes del rosco seleccionadas aleatoriamente
    Precondiciones: La lista y el diccionario deben estar cargados previamente.
    Postcondiciones: Obtencion de las palabras y definiciones que van a pertenecer a las letras participantes del rosco
    Autores: Valentín Marturet / Renato Villalba / Valentina Llanos Pontaut
    '''
    palabrasydefiniciones_seleccionadas = []
    palabras = diccionario_palabras_definicion.keys()
    palabras_filtradas = filtrar_palabras(palabras, palabras_por_letra, letras_participantes)
    CANT = 1
    indice = 0
    for letra_cant in palabras_por_letra:
        indice_random = random.randrange(indice, indice+letra_cant[CANT])
        palabra_definicion = [palabras_filtradas[indice_random], diccionario_palabras_definicion[palabras_filtradas[indice_random]]]
        palabrasydefiniciones_seleccionadas.append(palabra_definicion)
        indice += letra_cant[CANT]
    return palabrasydefiniciones_seleccionadas