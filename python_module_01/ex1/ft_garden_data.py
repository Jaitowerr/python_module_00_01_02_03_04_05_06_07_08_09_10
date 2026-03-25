#!/usr/bin/env python3

class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age_days = age

    def show(self) -> None:
        print(f' - {self.name}: {self.height}cm, {self.age_days} days old')


def main() -> None:
    p1 = Plant('Rosa', 25, 30)
    p2 = Plant('Sunflower', 80, 45)
    p3 = Plant('Cactus', 15, 120)

    garden = [p1, p2, p3]

    print('=== Garden Plant Registry ===')
    for i in garden:
        i.show()


if __name__ == "__main__":
    main()
