#!/usr/bin/env python3

class SecurePlant:

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height = self._validate_height(height)
        self._age_days = self._validate_age(age)

    def _validate_height(self, height: float) -> float:
        if height <= 0:
            return 0.0
        return round(height, 2)

    def _validate_age(self, age: int) -> int:
        if age <= 0:
            return 0
        return age

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, value: int) -> None:
        if value < 0:
            msg = f'**{self.name}: Error, height can''t be negative'
            print(msg)
            print('***Height update rejected')

        else:
            self._height = round(value, 2)
            print(f' - Height updated: {self.get_height()}cm')

    def set_age(self, value: int) -> None:
        if value < 0:
            msg = f'**{self.name}: Error, age can''t be negative'
            print(msg)
            print('***Age update rejected')

        else:
            self    ._age_days = value
            print(f' - Age updated: {self.get_age()} days')

    def get_info(self) -> str:
        h = self.get_height()
        a = self.get_age()
        return f'\nCurrent plant: {self.name} ({h}cm, {a} days)'


def main() -> None:
    print('=== Garden Security System ===')

    rose = SecurePlant('Rose', 15, 10)
    print(f'- Plant created: {rose.name}, {rose.get_height()}cm,'
          f' {rose.get_age()} days')

    print()
    rose.set_height(25)
    rose.set_age(30)

    print()
    rose.set_height(-5)
    rose.set_age(-500)

    print(rose.get_info())


if __name__ == '__main__':
    main()
