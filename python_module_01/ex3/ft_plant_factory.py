#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def get_info(self) -> str:
        return (f'{self.name}: {round(self.height, 2)}cm, '
                f'{self.age_days} days old.')

    def show(self) -> None:
        print(f'  - Created: {self.get_info()}')


def main() -> None:
    plant_data = [
        ('Rose', 25.0, 30),
        ('Oak', 200.0, 365),
        ('Cactus', 5.0, 90),
        ('Sunflower', 80.0, 45),
        ('Fern', 15.0, 120)
    ]

    print('=== Plant Factory Output ===')

    count = 0
    garden = []
    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plant.show()
        garden += [0]
        garden[count] = plant
        count += 1

    print('\nNames of created plants:', end='')
    i = 0
    for plant in garden:
        if i < (count - 1):
            print(f' {plant.name},', end='')
            i += 1
        else:
            print(f' {plant.name}.')

    print(f'\nTotal plants created: {count}')


if __name__ == '__main__':
    main()
