#! /usr/bin/env python3

import sys


def main() -> None:
    print('=== ARCHIVOS CIBERNÉTICOS - SISTEMA DE COMUNICACIÓN ===\n')
    try:
        id = input('Entrada de flujo activa. Ingrese ID del archivo: ')
        id_estado = input('Entrada de flujo activa. '
                          'Ingrese informe de estado: ')
        print(f'\n[ESTÁNDAR] Estado del archivo de {id}: {id_estado}',
              file=sys.stdout)
        print('***[ALERTA] Diagnóstico del sistema:'
              'Canales de comunicación verificados', file=sys.stderr)
        print('[ESTÁNDAR] Transmisión de datos completada\n', file=sys.stdout)

        print('     ---- Prueba de comunicación de tres canales exitosa. ----')
    except EOFError:
        print('Error: entrada interrumpida', file=sys.stderr)


if __name__ == '__main__':
    main()
