#! /usr/bin/env python3

def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS -SISTEMA DE SEGURIDAD DE LA BÓVEDA ===\n')
    print('Iniciando acceso seguro a la bóveda...')

    try:
        print('Conexión a la bóveda establecida con protocolos de seguridad\n')
        url = '../data-generator-tools/classified_data.txt'
        with open(url, 'r') as archive:
            print('EXTRACCIÓN SEGURA:')
            print(archive.read(), '\n')

        url = '../data-generator-tools/security_protocols.txt'
        with open(url, 'a') as archive:
            print('SECURE PRESERVATION:')
            archive.write('\nLa bóveda se sella automáticamente al finalizar')
        with open(url, 'r') as archive:
            print(archive.read())

    except FileNotFoundError:
        print('Error: archivo no encontrado')
    except PermissionError:
        print('Error: no tienes permisos')

    finally:
        print('\nTodas las operaciones de la bóveda completadas '
              'con máxima seguridad')


if __name__ == '__main__':
    main()
