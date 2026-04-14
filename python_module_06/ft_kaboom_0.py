from alchemy.grimoire import light_spell_record

try:
    print('=== Kaboom 0 ===')
    print('Using grimoire module directly')
    result = light_spell_record("Fantasy", "Earth, wind and fire")
    print(f'Testing record light spell: {result}')
except Exception as e:
    print(f' - ERROR: {e}')
