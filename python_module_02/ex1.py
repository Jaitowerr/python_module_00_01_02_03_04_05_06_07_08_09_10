#!/usr/bin/env python3

def input_temperature(temp_str: str) -> None:
    
    try:
        temp = int(temp_str)
        if temp:
            print(f'''\nInput data is '{temp}' ''')
            print(f'Temperature is now {temp}°C')
    except:
        print(f'''Input data is '{temp_str}' ''')
        print(f'''Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}' ''')


def test_temperature() -> None:
    print('=== Garden Temperature ===')
    input_temperature('25')
    input_temperature('abc')
    print('\nAll tests completed - program didn''t crash!')


if __name__ == '__main__':
    test_temperature()
