#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, msg: str = 'Unknow garden error') -> None:
        super().__init__(msg)


class PlantError(GardenError):
    def __init__(self, msg: str = 'Unknown plant error') -> None:
        # self.msg = msg
        super().__init__(msg)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f'''Invalid plant name to water: '{plant_name}' ''')
    print(f' - Watering {plant_name}: [OK]')


def test_watering_system() -> None:
    print('\n'
          '===================================\n'
          '=== Sistema de Riego del Jardín ===\n'
          '===================================\n'
          '\n')

    plants = ['Tomato', 'Lettuce', 'Carrots']

    try:
        print('***********************************************\n'
              '*********** Testing valid plants... ***********\n'
              '***********************************************\n\n'
              'Opening watering system')

        for plant in plants:
            water_plant(plant)

    except PlantError as e:
        print(f'Caught PlantError: {e}')
        print('.. ending tests and returning to main')
        return

    finally:
        print('------------------Closing watering system-----------------')

    print('\n\n')

    plants_two = ['Tomato', 'lettuce', 'Carrots']
    try:
        print('***********************************************\n'
              '********** Testing invalid plants... **********\n'
              '***********************************************\n\n'
              'Opening watering system')
        for plant in plants_two:
            water_plant(plant)
    except PlantError as e:
        print(f'***Caught PlantError: {e}')
        print('.. ending tests and returning to main')
        return

    finally:
        print('------------------Closing watering system-----------------')

    print('\nCleanup always happens, even with errors!')


if __name__ == '__main__':
    test_watering_system()
