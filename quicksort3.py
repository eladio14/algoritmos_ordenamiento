from objetos import *


def listar_archivos_carpetas_ordenados_por_tamaño(nombre_unidad, ubicacion, orden):
    """
    Lista los archivos y carpetas de una unidad de almacenamiento, ordenados por tamaño.

    Args:
      nombre_unidad: El nombre de la unidad de almacenamiento.
      ubicacion: La ubicación de los archivos y carpetas a listar.
      orden: El orden de los archivos y carpetas, ascendente o descendente.

    Returns:
      Una lista de archivos y carpetas ordenados por tamaño.
    """

    # Obtenemos la unidad de almacenamiento a partir del nombre.
    unidad = obtener_unidad_almacenamiento(nombre_unidad)

    # Obtenemos la lista de archivos y carpetas de la unidad.
    lista_archivos_carpetas = obtener_lista_archivos_carpetas(unidad, ubicacion)

    # Ordenamos la lista de archivos y carpetas por tamaño.
    return quicksort(lista_archivos_carpetas, orden)


def quicksort(lista, orden):
    """
    Ordena una lista por tamaño, utilizando el algoritmo quicksort.

    Args:
      lista: La lista a ordenar.
      orden: El orden de la lista, ascendente o descendente.

    Returns:
      La lista ordenada.
    """

    # Si la lista tiene un solo elemento, la devolvemos.
    if len(lista) <= 1:
        return lista

    # El pivote será el primer elemento de la lista.
    pivote = lista[0]

    # Dividimos la lista en dos, según si los elementos son menores o mayores que el pivote.
    lista_menores = [elemento for elemento in lista if elemento.tamaño < pivote.tamaño]
    lista_mayores = [elemento for elemento in lista if elemento.tamaño >= pivote.tamaño]

    # Ordenamos las sublistas de elementos menores y mayores.
    lista_menores = quicksort(lista_menores, orden)
    lista_mayores = quicksort(lista_mayores, orden)

    # Devolvemos la lista ordenada, con el pivote en el medio.
    if orden == "asc":
        return lista_menores + [pivote] + lista_mayores
    else:
        return lista_mayores + [pivote] + lista_menores


# Obtenemos la unidad de almacenamiento C:.
unidad_c = obtener_unidad_almacenamiento("C:")

# Listamos los archivos y carpetas de la carpeta C:/Documentos, ordenados por tamaño ascendente.
lista_archivos_carpetas = listar_archivos_carpetas_ordenados_por_tamaño(
    "C:", "C:/Documentos", "asc"
)

# Imprimimos la lista de archivos y carpetas.
for archivo_carpeta in lista_archivos_carpetas:
    print(archivo_carpeta)
