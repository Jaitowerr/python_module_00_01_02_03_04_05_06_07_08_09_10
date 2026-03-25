#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self, cm: float) -> None:
        self.height = round(self.height + cm, 2)

    def age(self, days: int) -> None:
        self.age_days += days

    def get_info(self) -> str:
        return (f'{self.name}: {round(self.height, 2)}cm, '
                f'{self.age_days} days old')


def grow_and_age(object: Plant, grow: float, day: int) -> None:
    print(f'\n=={object.name}==')
    day_one_height = object.height
    for day in range(1, day + 1):
        print(f'  === Day {day} ===')
        print(f'    {object.get_info()}')
        object.grow(grow)
        object.age(1)
    total_height = round(object.height - day_one_height, 2)
    print(f'Growth this week: +{total_height}cm')


def main() -> None:
    p1 = Plant('Rose', 25.0, 30)
    p2 = Plant('Sunflower', 80.0, 45)
    p3 = Plant('Cactus', 15.0, 120)

    print('=== Garden Plant Growth ===')

    grow_and_age(p1, 0.8, 7)
    grow_and_age(p2, 2, 7)
    grow_and_age(p3, 5, 7)


if __name__ == '__main__':
    main()
