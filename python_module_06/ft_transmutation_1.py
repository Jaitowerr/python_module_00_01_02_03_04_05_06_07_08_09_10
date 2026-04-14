import alchemy.transmutation

try:
    print('=== Transmutation 1 ===')
    print('Import transmutation module directly')
    print(f'Testing lead to gold: {alchemy.transmutation.lead_to_gold()}\n')
except Exception as e:
    print(f' - ERROR EN FT_TRANSMUTATION_1: {e}\n')
