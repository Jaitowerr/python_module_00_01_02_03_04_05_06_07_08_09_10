#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 2)}cm,'
              f' {self.age_days} days old')

    def grow(self, cm: float) -> None:
        self.height += cm

    def age(self, days: int) -> None:
        self.age_days += days


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        self._is_blooming = True
        print(f'**[asking the {self.name} to bloom]')

    def show(self) -> None:
        super().show()
        print(f' - Color: {self.color}')
        if self._is_blooming:
            print(f' - {self.name} is blooming beautifully!')
        else:
            print(f' - {self.name} has not bloomed yet')


class Tree(Plant):

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = False

    def produce_shade(self) -> None:
        self.shade = True
        print(f'**[asking the {self.name} to produce shade]')
        print(f'Tree {self.name} now produces a shade of {self.height}cm'
              f' long and {self.trunk_diameter} wide.')

    def show(self) -> None:
        super().show()
        print(f' - Trunk diameter: {self.trunk_diameter}cm')


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.har_season = harvest_season
        self.nutri_value = 0

    def grow(self, cm: float) -> None:
        super().grow(cm)

    def age(self, days: int) -> None:
        super().age(days)

    def grow_age(self, cm: float, days: int) -> None:
        self.grow(cm)
        self.age(days)
        self.nutri_value += 1 * days
        print(f'[make {self.name} grow and age for {days} days]')

    def show(self) -> None:
        super().show()
        print(f' - Harvest season: {self.har_season}')
        print(f' - Nutritional value: {self.nutri_value}')


def flower() -> None:
    print('\n=== FLOWER')

    rose = Flower('rose', 25.0, 10, 'red')

    rose.show()
    rose.bloom()
    rose.show()
    print()


def tree() -> None:
    print('\n=== TREE')

    oak = Tree('oak', 200.0, 365, 5.0)

    oak.show()
    oak.produce_shade()
    print()


def vegetable() -> None:
    print('\n=== VEGETABLE')

    tomato = Vegetable('tomato', 5.0, 10, 'April')
    # carrot = Vegetable('carrot', 30, 60, 'autumn')

    tomato.show()
    tomato.grow_age(42, 20)
    tomato.show()


def main() -> None:
    print('=== Garden Plant Types ===')
    flower()
    tree()
    vegetable()


if __name__ == '__main__':
    main()
