import alchemy

try:
    print('=== Distillation 1 ===')
    print('Using: \'import alchemy\' structure to access potions')
    print(f'Testing strength_potion: {alchemy.strength_potion()}')
    print(f'Testing heal alias: {alchemy.heal()}\n')
except Exception as e:
    print(f' - ERROR EN FT_DISTILLATION_1: {e}\n')
