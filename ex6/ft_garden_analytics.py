class Plant:
    def __init__(self, name: str):
        self.name = name
        self._height = 0
        self._old = 0

    class stats():
        def __init__(self):
            self.grow = 0
            self.age = 0
            self.show = 0

    @classmethod
    def create_anonymous(cls):
        return (Plant("anonymous"))

    def set_height(self, height_temp: float):
        if (height_temp < 0):
            print(f"Invalid operation attempted: {height_temp}cm [REJECTED]")
            print("Security: Negative height rejected")
            print("")
            return
        else:
            self._height = round(height_temp)

    def set_age(self, age_temp: int):
        if (age_temp < self._old):
            print(f"Invalid operation attempted: {age_temp} days [REJECTED]")
            print("Security: Can not rejuvenate")
        else:
            self._old = age_temp

    def grow(self):
        self._height += 0.8

    def age(self):
        self._old += 1

    def get_height(self):
        print(f"Current height of {self.name}: {self._height}cm")

    def show(self):
        print(f"Current age of {self.name}: {self._old} days")

    def get_status(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
    
    @staticmethod
    def check_year_old(age: int):
        print(f"Is {age} days more than a year ? -> ", end="")
        if (age < 365):
            print("False")
        else:
            print("True")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.color = color
        self.blooming = False

    def bloom(self):
        if not self.blooming:
            self.blooming = True

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Color: {self.color}")
        if not self.blooming:
            print(f"{self.name} has not bloomed yet")
        else:
            print("Rose is blooming beautifully!")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str, seeds: int):
        self.seeds_held = seeds


class tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.diameter = trunk_diameter

    def cast_shadow(self):
        print(f"Tree {self.name} produces a shade of", end="")
        print(f"{self._height}cm long and {self.diameter}cm wide.")

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Trunk diameter: {self.diameter}")


class vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.harvest_season = harvest_season
        self.nutrinional_value = 0

    def grow(self):
        temp_height = self._height + 2.1
        self.set_height(temp_height)

    def age(self):
        temp_age = self._old + 1
        self.set_age(temp_age)
        self.nutrinional_value += 1

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._old}days")
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutrinional_value}")

def display_statistics(name: Plant):
    name.stats.grow 


def main():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.check_year_old(30)
    Plant.check_year_old(400)
    print("")
    print("=== Flower")



if __name__ == "__main__":
    main()
