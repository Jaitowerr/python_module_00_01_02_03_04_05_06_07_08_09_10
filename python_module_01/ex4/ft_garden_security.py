class SecurePlant:

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = 0
        self._age_days = 0
        print(f' - Plant created: {self.name}')
        # No se debe pero se obliga para que aparezca primero
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age_days

    def set_height(self, value: int) -> None:
        if value < 0:
            salto = '\n'
            msg = f'**Invalid operation attempted: height {value}cm [REJECTED]'
            print(salto + msg)
            print('**Security: Negative height rejected')

        else:
            self._height = value
            print(f' - Height updated: {value}cm [OK]')

    def set_age(self, value: int) -> None:
        if value < 0:
            salto = '\n'
            msg = f'**Invalid operation attempted: age {value} days [REJECTED]'
            print(salto + msg)
            print('***Security: Negative age rejected')

        else:
            self._age_days = value
            print(f' - Age updated: {value} days [OK]')

    def get_info(self) -> str:
        h = self.get_height()
        a = self.get_age()
        return f'\nCurrent plant: {self.name} ({h}cm, {a} days)'


def main() -> None:
    print('=== Garden Security System ===')

    rose = SecurePlant('Rose', 50, 30)

    rose.set_height(-5)
    rose.set_age(-500)

    print(rose.get_info())


if __name__ == '__main__':
    main()
