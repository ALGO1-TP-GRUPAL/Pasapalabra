from datos import obtener_lista_definiciones

def crear_diccionario():
    """
    parametros = ??
    Postcondiciones = retorna un diccionario cuyas claves son las letras del abecedario y sus valores son todas las palabras que comienzan con esas mismas letras
    autores = Valle Valentin y Francisco Albinati 
    """
    PALABRA = 0
    DEFINICION = 1
    diccionario_de_palabras = {}
    lista_de_palabras = obtener_lista_definiciones()
    for palabra_definicion in lista_de_palabras:    
        if len(palabra_definicion[PALABRA]) >= 5:
            diccionario_de_palabras[palabra_definicion[PALABRA]] = palabra_definicion[DEFINICION]
    return diccionario_de_palabras

def palabra_sin_tilde(letra):
    """
    parametros = letra
    Postcondiciones = si la letra tiene tilde se le quita y nos devuelve la letra modificada, de no ser asi nos devuelve la misma letra
    autores = Valle Valentin y Francisco Albinati 
    """
    DICCIONARIO_TILDES = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    if letra in DICCIONARIO_TILDES:
        letra = DICCIONARIO_TILDES[letra]

    return letra

def mostrar_total_de_palabras(diccionario_de_palabras):
    """
    parametros = diccionario_de_palabras
    Postcondiciones = muestra en pantalla la cantidad de palabras que hay por letra y la cantidad total de palabras que hay en el diccionario_palabras
    autores = Valle Valentin y Francisco Albinati 
    """
    PRIMER_LETRA = 0
    diccionario_cantidad_por_letra = {}
    cantidad_palabras = len(diccionario_de_palabras)
    for palabra in diccionario_de_palabras:
        primer_letra_palabra = palabra_sin_tilde(palabra[PRIMER_LETRA])
        if primer_letra_palabra not in diccionario_cantidad_por_letra:
            diccionario_cantidad_por_letra[primer_letra_palabra] = 1
        else:
            diccionario_cantidad_por_letra[primer_letra_palabra] += 1

    # for letra in diccionario_cantidad_por_letra:
    #     print(f"la letra {letra} tiene {diccionario_cantidad_por_letra[letra]} letras")
    # print(cantidad_palabras)

    return diccionario_cantidad_por_letra

    



def etapa_2():   
    mostrar_total_de_palabras(crear_diccionario())

etapa_2()