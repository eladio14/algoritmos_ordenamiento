from objetos import *

class Gestion():
    def calcular_tamano_total(unidad: UnidadDeAlmacenamiento):
        total = 0
        for carpeta in unidad.lista_carpetas:
            total += carpeta.obtener_tamaño()
        return total

    def particion(lista, inicio, fin):
        pivot = lista[fin]
        i = inicio - 1
        for j in range(inicio, fin):
            if lista[j].tamaño_total <= pivot.tamaño_total:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
        lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
        return i + 1

    def quicksort(lista, inicio, fin):
        if inicio < fin:
            pi = Gestion.particion(lista, inicio, fin)
            Gestion.quicksort(lista, inicio, pi - 1)
            Gestion.quicksort(lista, pi + 1, fin)
    
    def dir(unidad: UnidadDeAlmacenamiento, ubicacion, orden):
        lista = unidad.lista_carpetas 
        if orden == 'asc':
            Gestion.quicksort(lista, 0, len(lista) - 1)
        else:
            lista.reverse()
        for item in lista:
            print(f"{item.nombre}: {item.tamaño_total}")

archivo1 = Archivo('1', 'documento1.txt', 1000, '.txt', '2024-01-29', '2024-01-29', 'Contenido del documento 1')
archivo2 = Archivo('2', 'documento2.docx', 2000, '.docx', '2024-01-29', '2024-01-29', 'Contenido del documento 2')
carpeta1 = Carpeta('3', 'Carpeta1', [], '2024-01-29', [])
carpeta2 = Carpeta('4', 'Carpeta2', [], '2024-01-29', [])

unidad = UnidadDeAlmacenamiento('1', 'C:', 10000, 7000, [carpeta1, carpeta2], 'HDD')

carpeta1.lista_ficheros.append(archivo1)
carpeta2.lista_ficheros.append(archivo2)

Gestion.dir(unidad, 'C:/', 'asc')