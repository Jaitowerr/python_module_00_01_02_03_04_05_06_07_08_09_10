#! /usr/bin/env python3

def main() -> None:
    print(' === ARCHIVOS CIBERNÉTICOS - SISTEMA DE RECUPERACIÓN DE DATOS ==='
          '\n')
    try:
        rut = '../data-generator-tools/ancient_fragment.txt'
        with open(f'{rut}', 'r') as archive:
            print('Accediendo al almacén de datos: '
                  f'{archive.name.split('/')[-1]}'
                  '\n')
            print('Conexión establecida...\n')
            print('Datos recuperados:')
            print(archive.read())
        print('\nRecuperación de datos completa de '
              f'{archive.name.split('/')[-1]} '
              'Unidad de almacenamiento desconectada.')
    except FileNotFoundError:
        print('Error: Almacén de almacenamiento o archivo no encontrado')


if __name__ == '__main__':
    main()
