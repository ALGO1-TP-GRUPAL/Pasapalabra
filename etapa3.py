from datos import obtener_lista_definiciones
import random

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
        if palabras[index][0].lower() in letras_seleccionadas:
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

    claves = sorted(diccionario_palabras.keys())
    claves_filtradas, letras_filtradas = filtrar_palabras(claves, cant_por_letra, letras_participantes)
    CANT = 1
    count = 0

    indice = 0
    for cant in letras_filtradas:
        rand = random.randrange(indice, indice+cant[CANT])
        palabra = [claves_filtradas[rand], diccionario_palabras[claves_filtradas[rand]]]
        palabras_seleccionadas.append(palabra)
        indice += cant[CANT]
        count += 1


    print(count)

    palabras_seleccionadas.sort()
    return palabras_seleccionadas




def main():
    lista_letras = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    # Todas estas variables fueron declaradas para probar la funcion - Luego borrar
    prueba_definiciones = {
    "A1": "Definicion A1",
    "A2": "Definicion A2",
    "A3": "Definicion A3",
    "A4": "Definicion A4",
    "B1": "Definicion B1",
    "B2": "Definicion B2",
    "B3": "Definicion B3",
    "B4": "Definicion B4",
    "C1": "Definicion C1",
    "C2": "Definicion C2",
    "C3": "Definicion C3",
    "C4": "Definicion C4",
    "D1": "Definicion D1",
    "D2": "Definicion D2",
    "D3": "Definicion D3",
    "D4": "Definicion D4",
    "E1": "Definicion E1",
    "E2": "Definicion E2",
    "E3": "Definicion E3",
    "E4": "Definicion E4",
    "F1": "Definicion F1",
    "F2": "Definicion F2",
    "F3": "Definicion F3",
    "F4": "Definicion F4",
    "G1": "Definicion G1",
    "G2": "Definicion G2",
    "G3": "Definicion G3",
    "G4": "Definicion G4",
    "H1": "Definicion H1",
    "H2": "Definicion H2",
    "H3": "Definicion H3",
    "H4": "Definicion H4",
    "I1": "Definicion i1",
    "I2": "Definicion i2",
    "I3": "Definicion I3",
    "I4": "Definicion I4",
    "J1": "Definicion J1",
    "J2": "Definicion J2",
    "J3": "Definicion J3",
    "J4": "Definicion J4",
    "K1": "Definicion k1",
    "K2": "Definicion K2",
    "K3": "Definicion K3",
    "K4": "Definicion K4",
    "L1": "Definicion L1",
    "L2": "Definicion L2",
    "L3": "Definicion L3",
    "L4": "Definicion L4",
    "M1": "Definicion M1",
    "M2": "Definicion M2",
    "M3": "Definicion M3",
    "M4": "Definicion M4",
    "N1": "Definicion N1",
    "N2": "Definicion N2",
    "N3": "Definicion N3",
    "N4": "Definicion N4",
    "Ñ1": "Definicion Ñ1",
    "Ñ2": "Definicion Ñ2",
    "Ñ3": "Definicion Ñ3",
    "Ñ4": "Definicion Ñ4",
    "O1": "Definicion O1",
    "O2": "Definicion O2",
    "O3": "Definicion O3",
    "O4": "Definicion O4",
    "P1": "Definicion P1",
    "P2": "Definicion P2",
    "P3": "Definicion P3",
    "P4": "Definicion P4",
    "Q1": "Definicion Q1",
    "Q2": "Definicion Q2",
    "Q3": "Definicion Q3",
    "Q4": "Definicion Q4",
    "R1": "Definicion R1",
    "R2": "Definicion R2",
    "R3": "Definicion R3",
    "R4": "Definicion R4",
    "S1": "Definicion S1",
    "S2": "Definicion S2",
    "S3": "Definicion S3",
    "S4": "Definicion S4",
    "T1": "Definicion T1",
    "T2": "Definicion T2",
    "T3": "Definicion T3",
    "T4": "Definicion T4",
    "U1": "Definicion U1",
    "U2": "Definicion U2",
    "U3": "Definicion U3",
    "U4": "Definicion U4",
    "V1": "Definicion V1",
    "V2": "Definicion V2",
    "V3": "Definicion V3",
    "V4": "Definicion V4",
    "W1": "Definicion W1",
    "W2": "Definicion W2",
    "W3": "Definicion W3",
    "W4": "Definicion W4",
    "X1": "Definicion X1",
    "X2": "Definicion X2",
    "X3": "Definicion X3",
    "X4": "Definicion X4",
    "Y1": "Definicion Y1",
    "Y2": "Definicion Y2",
    "Y3": "Definicion Y3",
    "Y4": "Definicion Y4",
    "Z1": "Definicion Z1",
    "Z2": "Definicion Z2",
    "Z3": "Definicion Z3",
    "Z4": "Definicion Z4",
}
    dicionario = {'ananá' : 'Fruta amarilla y ácida', 'barrer' : 'Acción de limpiar con una escoba', 'café' : 'Bebida con cafeína', 'dedo' : 'Parte de la mano', 'elfo' : 'Ser mítico con orejas puntiagudas', 'foco' : 'Objeto que ilumina una habitación'}
    lista_letras_1 = ['a', 'b', 'c', 'd', 'e', 'f']
    prueba_cantidades = [[letra, 4] for letra in lista_letras]

    letras_seleccionadas = crear_lista_letras(lista_letras)

    palabras_definiciones = seleccionar_palabra(prueba_definiciones, letras_seleccionadas, prueba_cantidades)

    print(letras_seleccionadas)
    print(palabras_definiciones)


main()