from cryptography.fernet import Fernet

# Función para generar una clave y guardarla en un archivo
def generar_clave(ruta):
    clave = Fernet.generate_key()
    with open(ruta, 'wb') as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave desde un archivo
def cargar_clave(ruta):
    return open(ruta, 'rb').read()

# Función para cifrar un archivo y guardar el contenido cifrado en un archivo .bin
def cifrar_archivo(ruta_archivo_original, ruta_archivo_bin, clave):
    fernet = Fernet(clave)
    with open(ruta_archivo_original, 'rb') as archivo_original:
        contenido = archivo_original.read()
    contenido_cifrado = fernet.encrypt(contenido)
    with open(ruta_archivo_bin, 'wb') as archivo_bin:
        archivo_bin.write(contenido_cifrado)

# Función para descifrar un archivo .bin y guardar el contenido descifrado en su formato original
def descifrar_archivo(ruta_archivo_bin, ruta_archivo_original, clave):
    fernet = Fernet(clave)
    with open(ruta_archivo_bin, 'rb') as archivo_bin:
        contenido_cifrado = archivo_bin.read()
    contenido_descifrado = fernet.decrypt(contenido_cifrado)
    with open(ruta_archivo_original, 'wb') as archivo_original:
        archivo_original.write(contenido_descifrado)

if __name__ == "__main__":
    while True:
        print('Opciones')
        print(' 1. Cifrar')
        print(' 2. Descifrar')
        print(' 3. Generar clave')
        print(' x salir')
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            ruta_archivo_original = input('Ruta del archivo original: ')
            ruta_archivo_bin = input('Ruta del archivo .bin: ')
            ruta_clave = input('Ruta del archivo de la clave: ')
            clave = cargar_clave(ruta_clave)
            cifrar_archivo(ruta_archivo_original, ruta_archivo_bin, clave)
            print('Archivo cifrado correctamente.')
        
        elif opcion == '2':
            ruta_archivo_bin = input('Ruta del archivo .bin cifrado: ')
            ruta_archivo_final = input('Ruta del archivo descifrado: ')
            ruta_clave = input('Ruta del archivo de la clave: ')
            clave = cargar_clave(ruta_clave)
            descifrar_archivo(ruta_archivo_bin, ruta_archivo_final, clave)
            print('Archivo descifrado correctamente.')
        
        elif opcion == '3':
            ruta_clave = input('Nombre o ruta del archivo para guardar la clave: ')
            generar_clave(ruta_clave)
            print(f'Clave generada y guardada en {ruta_clave}.')

        elif opcion == 'x':
            break
        else:
            print('Opción no válida. Intente de nuevo.')
