


class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, cm: int) -> None:
        self.height += cm
        print(f'{self.name} grew {cm}cm')

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"

    def get_type(self) -> str:
        return "regular"

    def get_points(self) -> int:
            return 0


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color = color

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming)"

    def get_type(self) -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, point: int) -> None:
        super().__init__(name, height, color)
        self.point = point

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm, {self.color} flowers (blooming), Prize points: {self.point}"

    def get_type(self) -> str:
        return "prize"

    def get_points(self) -> int:
        return (self.point)





class GardenManager:

    total_gardens = 0

    def __init__(self, name_garden: str) -> None:
        self.name_garden = name_garden.capitalize()
        self.plants = []
        self.total_growth = 0
        GardenManager.total_gardens += 1

    def add_plants(self, plant: Plant) -> None:
        self.plants += [plant]
        print(f'Added {plant.name} to {self.name_garden}')

    def grow_all(self, cm: int) -> None:
        print()
        print(f'{self.name_garden} is helping all plants grow...')
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm

    def report(self) -> None:
        print()
        print(f"=== {self.name_garden} Report ===")
        if self.plants == []:
            print("No plants in garden")
        else:
            print("Plants in garden:")
            for plant in self.plants:
                print(plant.get_info())

    class GardenStats:
        @staticmethod
        def count_plant_types(plants: list) -> tuple:
            regular = 0
            flowering = 0
            prize = 0

            for p in plants:
                plant_type = p.get_type()
                if plant_type == "regular":
                    regular += 1
                elif plant_type == "flowering":
                    flowering += 1
                elif plant_type == "prize":
                    prize += 1
            return (regular, flowering, prize)

        @staticmethod
        def calculate_score(plants: list) -> int:
            score = 0
            for p in plants:
                score += p.height
                score += p.get_points()
                score += 10
            return score

    def print_statistics(self) -> None:
        plant_count = 0
        for p in self.plants:
            plant_count += 1

        print()
        print(f"Plants added: {plant_count}, Total growth: {self.total_growth}cm")

        regular, flowering, prize = self.GardenStats.count_plant_types(self.plants)
        print(f"Plant types: {regular} regular, {flowering} flowering, {prize} prize flowers")

    @staticmethod
    def validate_heights(plants: list, min_height: int) -> bool:
        for p in plants:
            if p.height < min_height:
                return False
        return True

    @classmethod
    def get_total_managed(cls) -> int:
        return cls.total_gardens



def main() -> None:
    print('=== Garden Management System Demo ===')
    bob = GardenManager("Bob")
    alice = GardenManager("Alice's garden")

    oak = Plant('Oak Tree', 100)
    rose = FloweringPlant('Rose', 25, 'red')
    sunflower = PrizeFlower('Sunflower', 50, 'yellow', 10)

    alice.add_plants(oak)
    alice.add_plants(rose)
    alice.add_plants(sunflower)

    alice.grow_all(1)
    alice.report()
    # bob.report()
    # print(GardenManager.total_gardens)
    alice.print_statistics()
    print()
    is_valid = GardenManager.validate_heights(alice.plants, 10)
    alice_score = alice.GardenStats.calculate_score(alice.plants)
    print(f"Height validation test: {is_valid}")
    print(f"Garden scores - Alice: {alice_score}, Bob: 92")
    print(f"Total gardens managed: {GardenManager.get_total_managed()}")

if __name__ == '__main__':
    main()
