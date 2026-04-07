#! /usr/bin/env python3

def secure_archive(filename: str,
                   action: str = 'read',
                   content: str = ''
                   ) -> tuple[bool, str]:
    try:
        if filename:
            if action == 'write':
                with open(filename, 'a') as file:
                    file.write(content)
                return (True, 'Contenido escrito correctamente en el archivo')
            elif action == 'read':
                with open(filename, 'r') as file:
                    data = file.read()
                return (True, data)
            else:
                raise Exception('Acción no válida, read o write')
        else:
            raise Exception('Filename no puede estar vacío')

    except Exception as e:
        return (False, str(e))


def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS -SISTEMA DE SEGURIDAD ===\n')

    print('Iniciando acceso seguro a la bóveda...\n')

    print('Usando \'secure_archive\' para leer desde un archivo inexistente:')
    print(secure_archive('/not/existing/file'))
    print()

    print('Usando \'secure_archive\' para leer desde un archivo inaccesible:')
    print(secure_archive('/root/secret.txt'))
    print()

    print('Usando \'secure_archive\' para leer desde un archivo')
    print(secure_archive('ancient_fragment.txt',
                         'read',
                         'Contenido de prueba'))
    print()

    print('Usando \'secure_archive\' para escribir contenido')
    print(secure_archive('new_archive_writea.txt',
                         'write',
                         'Contenido de prueba\n'))
    print()

    print(secure_archive('new_archive_writea.txt'))


if __name__ == '__main__':
    main()
