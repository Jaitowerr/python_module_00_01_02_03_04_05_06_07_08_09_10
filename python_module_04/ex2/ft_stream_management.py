#! /usr/bin/env python3

import sys


def ft_ancient_text(filename: str) -> None:
    print(' === ARCHIVOS CIBERNÉTICOS - RECUPERACIÓN Y PERSEVARACIÓN ===\n')
    archive = None

    try:
        print(f'Accediendo al archivo: \'{filename}\'\n')
        archive = open(filename, 'r')
        print('Conexión establecida... Datos recuperados:\n')
        print(archive.read())

    except (PermissionError, FileNotFoundError) as e:
        print(f'[STDERR] Error al abrir el archivo \'{filename}\': {e}',
              file=sys.stderr)

    finally:
        if archive:
            archive.close()
            print(f'\n----\nArchivo \'{filename}\' cerrado.')
            new_archive(filename)


def new_archive(filename: str) -> None:
    print('\nTransformar datos:\n---\n')
    archive_read = None
    archive_new = None

    try:
        archive_read = open(filename, 'r')
        content = archive_read.read()
        for line in content.splitlines():
            print(line + '#')
        sys.stdout.write('\n---\nIntroduce un nuevo nombre '
                         'de archivo (o deja vacío): ')
        sys.stdout.flush()
        name = sys.stdin.readline().strip()
        if name:
            archive_new = open(name, 'w')
            lines = content.splitlines()
            for line in lines:
                if line == lines[-1]:
                    archive_new.write(line + '#')
                else:
                    archive_new.write(line + '#\n')
            print('Guardando datos en ', name, '.')
            print('Datos guardados en el archivo ', name, '.')
        else:
            print('No se guardarán los datos.')

    except OSError as e:
        print(f'[STDEeeRR] Error al abrir el archivo \'{name}\': {e}',
              file=sys.stderr)

    finally:
        if archive_read:
            archive_read.close()
        if archive_new:
            archive_new.close()


def main() -> None:
    if len(sys.argv) != 2:
        print('Por favor, usa: ft_stream_management.py <file>')
        return
    ft_ancient_text(sys.argv[1])


if __name__ == '__main__':
    main()
