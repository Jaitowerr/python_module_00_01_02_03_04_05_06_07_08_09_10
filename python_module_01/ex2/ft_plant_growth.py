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
        return f'{self.name}: {round(self.height, 2)}cm, {self.age_days} days old'

def printt(name: str, grow: float, age: int, range: int) -> None:
    pass

def main() -> None:
    p1 = Plant('Rose', 25.0, 30)
    p2 = Plant('Sunflower', 80.0, 45)
    p3 = Plant('Cactus', 15.0, 120)

    garden = [p1, p2, p3]
    print('=== Garden Plant Growth ===')
    for plant in garden:
        print(f'====={plant.name}=====')
        day_one_height = plant.height
        for day in range(1, 8):
            if day == 1 or day == 7:
                print(f'  === Day {day} ===')
                print(f'    {plant.get_info()}')
            plant.grow(0.8)
            plant.age(1)
        total_height = round(plant.height - day_one_height)
        print(f'Growth this week: +{total_height}cm')
        print()


if __name__ == '__main__':
    main()
