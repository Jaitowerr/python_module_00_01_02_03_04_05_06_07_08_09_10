from alchemy.potions import healing_potion, strength_potion

try:
    print('=== Distillation 0 ===')
    print('Direct access to alchemy/potions.py')
    print(f'Testing strength_potion: {strength_potion()}')
    print(f'Testing healing_potion: {healing_potion()}\n')
except Exception as e:
    print(f' - ERROR EN FT_DISTILLATION_0: {e}\n')
