class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age


def main() -> None:
    garden = [
        ('Rose', 25, 30),
        ('Oak', 200, 365),
        ('Cactus', 5, 90),
        ('Sunflower', 80, 45),
        ('Fern', 15, 120)
    ]

    print('=== Plant Factory Output ===')
    count_garden = 0

    for i in garden:
        count_garden += 1

    garden_objects = [None] * count_garden
    count = 0
    for i in range(count_garden):
        p = Plant(garden[i][0], garden[i][1], garden[i][2])
        garden_objects[i] = p
        count += 1
        print(f'  - Created: {p.name} ({p.height}cm, {p.age_days} days)')

    print('\nNames of created plants: ', end='')
    for i in range(count_garden):
        if i < count_garden - 1:
            print(f'{garden_objects[i].name}, ', end='')
        else:
            print(garden_objects[i].name)

    print(f'\nTotal plants created: {count}')


if __name__ == '__main__':
    main()
