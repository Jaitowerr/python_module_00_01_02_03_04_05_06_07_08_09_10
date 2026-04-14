import alchemy.transmutation.recipes

try:
    print('=== Transmutation 0 ===')
    print('Using file alchemy/transmutation/recipes.py directly')
    result = alchemy.transmutation.recipes.lead_to_gold()
    print(f'Testing lead to gold: {result}\n')
except Exception as e:
    print(f' - ERROR EN FT_TRANSMUTATION_0: {e}\n')
