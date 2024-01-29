from objetos import *


def listar_ficheros_carpetas(unidad_almacenamiento, ubicación, orden):
    lista_ficheros_carpetas = []

    for carpeta in unidad_almacenamiento.lista_carpetas:
        if carpeta.nombre == ubicación:
            lista_ficheros_carpetas.extend(carpeta.lista_ficheros)
            lista_ficheros_carpetas.extend(carpeta.lista_carpetas)

    if orden == "asc":
        quicksort(lista_ficheros_carpetas, 0, len(lista_ficheros_carpetas) - 1, True)
    elif orden == "desc":
        quicksort(lista_ficheros_carpetas, 0, len(lista_ficheros_carpetas) - 1, False)

    print(lista_ficheros_carpetas)
    return lista_ficheros_carpetas

def quicksort(lista, inicio, fin, ascendente):
    if inicio < fin:
        indice_pivote = particion(lista, inicio, fin, ascendente)
        quicksort(lista, inicio, indice_pivote - 1, ascendente)
        quicksort(lista, indice_pivote + 1, fin, ascendente)

def particion(lista, inicio, fin, ascendente):
    pivote = lista[fin].tamaño
    i = inicio - 1
    for j in range(inicio, fin):
        if (ascendente and lista[j].tamaño <= pivote) or (not ascendente and lista[j].tamaño >= pivote):
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1


archivo1 = Archivo('1', 'documento1.txt', 1000, '.txt', '2024-01-29', '2024-01-29', 'Contenido del documento 1')
archivo2 = Archivo('2', 'documento2.docx', 2000, '.docx', '2024-01-29', '2024-01-29', 'Contenido del documento 2')
carpeta1 = Carpeta('3', 'Carpeta1', [], '2024-01-29', [])
carpeta2 = Carpeta('4', 'Carpeta2', [], '2024-01-29', [])

carpeta1.lista_ficheros.append(archivo1)
carpeta2.lista_ficheros.append(archivo2)

unidad = UnidadDeAlmacenamiento('1', 'C:', 10000, 7000, [carpeta1, carpeta2], 'HDD')

lista_ficheros_carpetas = listar_ficheros_carpetas(unidad, "C:/Documentos", "asc")