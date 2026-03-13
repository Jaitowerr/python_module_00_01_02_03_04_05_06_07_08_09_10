class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age_days = age

    def get_info(self) -> str:
        return f'{self.name}: {self.height}cm, {self.age_days} days'


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        print(f' - {self.name} is blooming beautifully in {self.color}!')

    def get_info(self) -> str:
        info_padre = super().get_info()
        return info_padre + f', {self.color} color'


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.5
        print(f' -{self.name} provides {shade} square meters of shade')

    def get_info(self) -> str:
        base = super().get_info()
        return f'{base}, {self.trunk_diameter}cm diameter'


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.har_season = harvest_season
        self.nutri_value = nutritional_value

    def harvest_info(self) -> None:
        print(f' - {self.name} is rich in {self.nutri_value}')

    def get_info(self) -> str:
        base = super().get_info()
        return f'{base}, {self.har_season} harvest'


def flower() -> None:
    print('\n=== FLOWER ===')

    rose = Flower('rose', 25, 30, 'red')
    tulip = Flower('tulip', 15, 20, 'yellow')

    print(rose.get_info())
    rose.bloom()
    print()
    print(tulip.get_info())
    tulip.bloom()


def tree() -> None:
    print('\n=== TREE ===')

    oak = Tree('oak', 500, 1825, 50)
    pine = Tree('pine', 300, 1000, 30)

    print(oak.get_info())
    oak.produce_shade()
    print()
    print(pine.get_info())
    pine.produce_shade()


def vegetable() -> None:
    print('\n=== VEGETABLE ===')

    tomato = Vegetable('tomato', 80, 90, 'summer', 'vitamin C')
    carrot = Vegetable('carrot', 30, 60, 'autumn', 'vitamin A')

    print(tomato.get_info())
    tomato.harvest_info()
    print()
    print(carrot.get_info())
    carrot.harvest_info()


if __name__ == '__main__':
    print('=== Garden Plant Types ===')
    flower()
    tree()
    vegetable()
