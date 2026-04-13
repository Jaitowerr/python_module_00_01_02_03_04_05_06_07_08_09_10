from alchemy.elements import create_air

try:
    print('=== Alembic 3 ===')
    print('Accessing alchemy/elements.py using \'from '
          '... import ...\' structure')
    print(f'Testing create_earth: {create_air()}\n')

except Exception:
    print(' - ERROR EN FT_ALEMBIC_3')
