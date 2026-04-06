#! /usr/bin/env python3

import sys


def ft_ancient_text(filename: str) -> None:
    print(' === ARCHIVOS CIBERNÉTICOS - SISTEMA DE RECUPERACIÓN DE DATOS ==='
          '\n')
    archive = None
    try:
        print('Accediendo al almacén de datos: '
              f'{filename}\n')
        archive = open(filename, 'r')
        print('Conexión establecida...\n'
              'Datos recuperados:\n')
        print(archive.read())
    except (PermissionError, FileNotFoundError) as e:
        print(f'Error al abrir el archivo \'{filename}\': {e}')
    finally:
        if archive:
            archive.close()
            print(f'\n----\nArchivo \'{filename}\' cerrado.')


def main() -> None:
    if len(sys.argv) != 2:
        print(f"Por favor, usa: {sys.argv[0].split('/')[-1]}.py <file>")
        return
    ft_ancient_text(sys.argv[1])


if __name__ == '__main__':
    main()
