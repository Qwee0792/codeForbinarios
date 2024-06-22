from cryptography.fernet import Fernet

# Función para generar una clave y guardarla en un archivo
def generar_clave(ruta):
    # Genera una nueva clave utilizando Fernet
    clave = Fernet.generate_key()
    # Guarda la clave en un archivo especificado por la ruta en modo escritura binaria ('wb')
    with open(ruta, 'wb') as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave desde un archivo
def cargar_clave(ruta):
    # Lee la clave desde el archivo especificado por la ruta en modo lectura binaria ('rb')
    return open(ruta, 'rb').read()

# Función para cifrar un archivo y guardar el contenido cifrado en un archivo .bin
def cifrar_archivo(ruta_archivo_original, ruta_archivo_bin, clave):
    # Crea un objeto Fernet usando la clave proporcionada
    fernet = Fernet(clave)
    # Abre el archivo original en modo lectura binaria ('rb')
    with open(ruta_archivo_original, 'rb') as archivo_original:
        # Lee todo el contenido del archivo original
        contenido = archivo_original.read()
    # Cifra el contenido usando el objeto Fernet
    contenido_cifrado = fernet.encrypt(contenido)
    # Abre o crea un archivo .bin en modo escritura binaria ('wb') y escribe el contenido cifrado
    with open(ruta_archivo_bin, 'wb') as archivo_bin:
        archivo_bin.write(contenido_cifrado)

# Función para descifrar un archivo .bin y guardar el contenido descifrado en su formato original
def descifrar_archivo(ruta_archivo_bin, ruta_archivo_original, clave):
    # Crea un objeto Fernet usando la clave proporcionada
    fernet = Fernet(clave)
    # Abre el archivo .bin cifrado en modo lectura binaria ('rb')
    with open(ruta_archivo_bin, 'rb') as archivo_bin:
        # Lee el contenido cifrado del archivo .bin
        contenido_cifrado = archivo_bin.read()
    # Descifra el contenido cifrado usando el objeto Fernet
    contenido_descifrado = fernet.decrypt(contenido_cifrado)
    # Abre o crea un archivo en modo escritura binaria ('wb') y escribe el contenido descifrado
    with open(ruta_archivo_original, 'wb') as archivo_original:
        archivo_original.write(contenido_descifrado)

# Programa principal
if __name__ == "__main__":
    # Bucle principal que se ejecuta continuamente hasta que el usuario elige salir ('x')
    while True:
        # Muestra las opciones disponibles
        print('Opciones')
        print(' 1. Cifrar')
        print(' 2. Descifrar')
        print(' 3. Generar clave')
        print(' x salir')
        # Solicita al usuario que seleccione una opción
        opcion = input('Seleccione una opción: ')
        
        if opcion == '1':
            # Opción para cifrar un archivo
            ruta_archivo_original = input('Ruta del archivo original: ')
            ruta_archivo_bin = input('Ruta del archivo .bin: ')
            ruta_clave = input('Ruta del archivo de la clave: ')
            clave = cargar_clave(ruta_clave)
            cifrar_archivo(ruta_archivo_original, ruta_archivo_bin, clave)
            print('Archivo cifrado correctamente.')
        
        elif opcion == '2':
            # Opción para descifrar un archivo
            ruta_archivo_bin = input('Ruta del archivo .bin cifrado: ')
            ruta_archivo_final = input('Ruta del archivo descifrado: ')
            ruta_clave = input('Ruta del archivo de la clave: ')
            clave = cargar_clave(ruta_clave)
            descifrar_archivo(ruta_archivo_bin, ruta_archivo_final, clave)
            print('Archivo descifrado correctamente.')
        
        elif opcion == '3':
            # Opción para generar una nueva clave y guardarla en un archivo
            ruta_clave = input('Nombre o ruta del archivo para guardar la clave: ')
            generar_clave(ruta_clave)
            print(f'Clave generada y guardada en {ruta_clave}.')

        elif opcion == 'x':
            # Opción para salir del programa
            break
        else:
            # Maneja la opción inválida
            print('Opción no válida. Intente de nuevo.')
