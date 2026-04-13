import alchemy.elements

try:
    print('=== Alembic 2 ===')
    print('Accessing alchemy/elements.py using \'import ...\' structure')
    print(f'Testing create_earth: {alchemy.elements.create_earth()}\n')

except Exception:
    print(' - ERROR EN FT_ALEMBIC_2')
