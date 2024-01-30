
def mergesort():
    print("1. Mostrar archivo")
    print("2. Mostrar carpeta")
    print("3. Ordenar archivos en una carpeta")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        id = input("Ingrese el ID del archivo: ")
        archivo = unidad_de_almacenamiento.buscar_archivo(id)
        if archivo is not None:
            archivo.mostrar()
        else:
            print("Archivo no encontrado.")
    elif opcion == "2":
        id = input("Ingrese el ID de la carpeta: ")
        carpeta = unidad_de_almacenamiento.buscar_carpeta(id)
        if carpeta is not None:
            carpeta.mostrar()
        else:
            print("Carpeta no encontrada.")
    elif opcion == "3":
        id = input("Ingrese el ID de la carpeta: ")
        archivos = unidad_de_almacenamiento.obtener_archivos_de_carpeta(id)
        if archivos:
            archivos_ordenados = merge_sort(archivos, 'fecha_modificacion')
            for archivo in archivos_ordenados:
                archivo.mostrar()
        else:
            print("No se encontraron archivos en esa carpeta.")
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, inténtelo de nuevo.")