from funciones import Funciones
import time

data = Funciones.obtener_data()

def login():
    print('LOGIN')
    nombre = input('Introduzca el Nombre de Usuario: ')
    contraseña = input('Introduzca su Contraseña: ')

    if (nombre == 'admin' and contraseña == 'admin'):
        menu_principal()
        return 
    if (nombre in data["usuarios"].keys()):
        if (data["usuarios"][nombre]):
            menu_principal()
            return
        else:
            print('Acceso denegado')
            time.sleep(1)
            login()
            return
    else:
        print('Acceso denegado')
        time.sleep(1)
        login()
        return

def menu_principal():
    print('MENU PRINCIPAL')
    print('Introduzca una de las siguientes opciones: ')
    print('1. Crear Usuario')
    print('2. Gestión de Ficheros y Carpetas')
    print('3. Resetear Datos')
    print('4. Crear Fichero')
    print('5. Crear Carpeta')
    print('6. Crear Unidad de Almacenamiento')
    print('7. Salir')
    
    opcion = int(input())

    if opcion == 1:
        menu_crear_usuario()
    elif opcion == 2:
        menu_gestion_ficheros()
    elif opcion == 4:
        menu_crear_fichero()
    elif opcion == 5:
        menu_crear_carpeta()
    elif opcion == 6:
        menu_crear_unidad()
    elif opcion == 7:
        exit()
    
def menu_crear_usuario():
    print('MENU CREAR USUARIO')
    print('Introduzca el Rol del Usuario: ')
    print('1. Administrador')
    print('2. Usuario Estandar')
    print('3. Regresar')

    opcion_rol = int(input())

    if opcion_rol == 3:
        menu_principal()
        return
    
    nombre_usuario = input('Introduzca el Nombre del Usuario: ')

    if nombre_usuario in data["usuarios"]:
        print('El usuario ya existe')
        menu_crear_usuario()
        return

    contraseña_usuario = input('Introduzca la Contraseña del Usuario: ')

    data["usuarios"][nombre_usuario] = {'rol': opcion_rol, 'contrasena': contraseña_usuario}

    Funciones.guardar_data(data)

    print('Usuario Creado con exito')

def menu_gestion_ficheros():
    print('MENU GESTIÓN DE FICHEROS Y CARPETAS')
    print('Introduzca una de las siguientes opciones: ')
    print('1. Listar ficheros y carpetas ordenados por tamaño')
    print('2. Mostrar  ficheros  y  carpetas  en  orden  de  fecha  de  última  modificación')
    print('3. Buscar ficheros o carpetas por rango de tamaño y extensión')
    print('4. Listar todos los ficheros y carpetas que sean mayores o menores que un tamaño específico dado por el usuario')
    print('5. Ordenar por fecha de creación carpetas y ficheros según una ubicación de forma')
    print('6. Regresar')

    opcion = int(input())

    if opcion == 2:
        mergesort()
    elif opcion == 6:
        menu_principal()

def menu_crear_fichero():
    ID = 0

def menu_crear_carpeta():
    pass

def menu_crear_unidad():
    pass

if __name__ == '__main__':
    login()