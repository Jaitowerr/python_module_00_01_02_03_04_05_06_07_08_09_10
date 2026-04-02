#! /usr/bin/env python3

def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS - SISTEMA DE PRESERVACIÓN ===')
    try:
        rut = '../new_discovery.txt'
        with open(rut, 'x') as archive:
            print('Inicializando nueva unidad de almacenamiento: '
                  f'{archive.name.split('/')[-1]}')
            print('Unidad de almacenamiento creada con éxito...\n')
            print('Escribiendo datos de entrada...')
            entry_one = '[ENTRY 001] New quantum algorithm discovered\n'
            entry_two = '[ENTRY 002] Efficiency increased by 347%\n'
            entry_three = '[ENTRY 003] Archived by Data Archivist trainee'
            archive.write(entry_one + entry_two + entry_three)
            print(entry_one + entry_two + entry_three)
        print('\nInscripción de datos completa. '
              'Unidad de almacenamiento sellada\n'
              f'Archivo: {archive.name.split('/')[-1]} '
              'listo para preservación a largo plazo.')
    except FileNotFoundError:
        print('***Error: la ruta no existe')
    except PermissionError:
        print('***Error: no tienes permisos para crear el archivo')
    except FileExistsError:
        print('***El archivo ya existe', rut.split('/')[-1])
        print('***Comprueba el archivo en la ruta:', rut)


if __name__ == '__main__':
    main()
