#!/usr/bin/env python3

class Plant:

    class Statistics:

        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self):
            print(f'Stats: {self.grow_calls} grow, {self.age_calls} age,'
                  f' {self.show_calls} show')

    def __init__(self, name: str, height: float, age_in_days: int = 0) -> None:
        self.name = name
        self.height = height
        self.age_in_days = age_in_days
        self.stats = Plant.Statistics()

    @staticmethod
    def is_older_year(age_in_days: int) -> bool:
        return age_in_days > 365

    @classmethod
    def anonymous(cls):
        return cls('Unknown plant', 0.0, 0)

    def grow(self, cm: float) -> None:
        self.height += cm
        self.stats.grow_calls += 1

    def age(self, days: int) -> None:
        self.age_in_days += days
        self.stats.age_calls += 1

    def show(self) -> None:
        self.stats.show_calls += 1
        print(f'{self.name}: {self.height}cm, {self.age_in_days} days old')


class Flower(Plant):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f' - Color: {self.color}')
        if self.bloomed:
            print(f' - {self.name} is blooming beautifully!')
        else:
            print(f' - {self.name} has not bloomed yet')
        self.stats.show_calls += 1


class Seed(Flower):

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f' - Seeds: {self.seeds}')
        self.stats.show_calls += 1


class Tree(Plant):

    def __init__(self, name: str, he: float, age: int, tr_d: float) -> None:
        super().__init__(name, he, age)
        self.trunk_diameter = tr_d
        self.shade_length = 0
        self.shade_width = 0
        self.shade_count = 0

    def produce_shade(self) -> None:
        self.shade_length = self.height
        self.shade_width = self.trunk_diameter * 2
        self.shade_count += 1
        print(f'Tree {self.name} now produces a shade of {self.shade_length}cm'
              f' long and {self.shade_width}cm wide.')

    def show(self) -> None:
        super().show()
        print(f' - Trunk diameter: {self.trunk_diameter}cm')
        self.stats.show_calls += 1
        print(f' - {self.shade_count} shade')


def display_statistics(plant: Plant) -> None:
    plant.stats.display()


def main():
    print('=== Garden statistics ===')

    print('=== Check year-old')
    print(f'Is 30 days more than a year? -> {Plant.is_older_year(30)}')
    print(f'Is 400 days more than a year? -> {Plant.is_older_year(400)}')
    print()

    print('=== Flower')
    rose = Flower('Rose', 15.0, 10, 'red')
    rose.show()
    display_statistics(rose)
    print('[asking the rose to grow and bloom]')
    rose.grow(8)
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print('=== Tree')
    oak = Tree('Oak', 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print('[asking the oak to produce shade]')
    oak.produce_shade()
    display_statistics(oak)
    print()

    print('=== Seed')
    sunflower = Seed('Sunflower', 80.0, 45, 'yellow')
    sunflower.show()
    display_statistics(sunflower)
    print('[make sunflower grow, age and bloom]')
    sunflower.grow(30)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print('=== Anonymous')
    unknown = Plant.anonymous()
    unknown.show()
    print('[statistics for Unknown plant]')
    display_statistics(unknown)


if __name__ == '__main__':
    main()
