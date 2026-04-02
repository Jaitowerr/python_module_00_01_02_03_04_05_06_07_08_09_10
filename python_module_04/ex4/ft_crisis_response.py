#! /usr/bin/env python3


def crisis_handler(rut: str) -> None:
    print('ALERTA DE CRISIS: Intentando acceder a', rut.split('/')[-1],
          '...')
    try:
        with open(rut, 'r') as archive:
            print('SUCCESS: Archive recovered - ', archive.read())
            print('ESTADO: Operaciones normales reanudadas\n')

    except FileNotFoundError:
        print('RESPUESTA: Archivo no encontrado '
              'en la matriz de almacenamiento\n'
              'ESTADO: Crisis gestionada, sistema estable\n')
    except PermissionError:
        print('RESPUESTA: Los protocolos de seguridad deniegan el acceso\n'
              'ESTADO: Crisis gestionada, seguridad mantenida\n')
    except Exception:
        print('RESPUESTA: Anomalía inesperada del sistema\n'
              'ESTADO: Crisis gestionada, sistema estable\n')


def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS - SISTEMA DE RESPUESTA A CRISIS ===\n')

    crisis_handler('lost_archive.txt')
    crisis_handler('classified_vault.txt')
    crisis_handler('../data-generator-tools/standard_archive.txt')

    sangría_izq = ' ' * 31
    linea = '-' * 54
    print(sangría_izq, linea)
    print(sangría_izq, '|Todos los escenarios de crisis manejados con éxito.|')
    print(sangría_izq, linea)


if __name__ == '__main__':
    main()
