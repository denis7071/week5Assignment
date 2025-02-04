class Speedster:
    # Base class for all speedsters with encapsulated properties
    def __init__(self, name, alias, universe, suit_color, experience=0):
        self._name = name  # Protected attribute
        self._alias = alias
        self.__experience = experience  # Private attribute
        self.universe = universe
        self.suit_color = suit_color
        self._level = 1

    def _level_up(self):
        if self.__experience >= 100:
            self._level += 1
            self.__experience -= 100
            return f"{self._alias} leveled up to Level {self._level}!"
        return None

    def get_experience(self):
        return self.__experience

    def display_info(self):
        return f"{self._alias} ({self._name}) from {self.universe}"

class Flash(Speedster):
    # Concrete Flash implementation with unique initialization
    def __init__(self, 
                 name="Barry Allen",
                 universe="Earth-1",
                 suit_color="Red",
                 allies=None,
                 enemies=None):
        super().__init__(name, "The Flash", universe, suit_color)
        self.abilities = ["Super Speed", "Time Travel", "Phasing", "Tornado Generation"]
        self.current_speed = 0
        self.max_speed = 670_616_629
        self.energy = 100
        self.allies = allies or ["Iris West", "Cisco Ramon", "Batman"]
        self.enemies = enemies or ["Reverse Flash", "Zoom", "Savitar"]
        self._phasing_duration = 0

    def generate_lightning(self, target):
        if self.energy >= 40:
            self.energy -= 40
            return f"Lightning attack on {target}. Energy: {self.energy}%"
        return "Low energy - recharge required"

    def team_attack(self, ally):
        if ally in self.allies:
            return f"Team attack with {ally}: Speed {self.current_speed * 1.5}mph"
        return "Ally not recognized"

    def _handle_enemy(self, enemy):
        if enemy in self.enemies:
            return f"Engaging {enemy} in combat"
        return "Enemy not in database"

    def display_info(self):  # Polymorphic implementation
        base_info = super().display_info()
        return f"{base_info}\nSuit: {self.suit_color} | Level: {self._level}"

class FutureFlash(Flash):
    # Inherited class demonstrating method overriding
    def __init__(self):
        super().__init__(
            name="Bart Allen",
            universe="Earth-25",
            suit_color="Silver-Red",
            allies=["Superman (Future)", "AI Gideon"],
            enemies=["Reverse Flash (AI)", "Time Wraiths"]
        )
        self.abilities.append("Chronal Duplication")
        self.future_tech = ["Nanotech Suit", "Speed Force Battery"]

    def generate_lightning(self, target):  # Overridden method
        return f"Chrono-lightning strike on {target} (temporal disruption)"

    def time_travel(self):  # Enhanced method
        return "Instantaneous time jump via chronal slipstream"

# Implementation example
if __name__ == "__main__":
    def hero_action(character):
        print(f"\n{character.display_info()}")
        print(character.generate_lightning("Reverse Flash"))
        if isinstance(character, FutureFlash):
            print(character.time_travel())

    barry = Flash(suit_color="Red-Gold")
    bart = FutureFlash()

    hero_action(barry)
    hero_action(bart)

    # Encapsulation test
    try:
        print(barry.__experience)
    except AttributeError:
        print("\nEncapsulation enforced: Experience attribute is private")

    # Alternate universe instance
    earth2_flash = Flash(
        name="Jay Garrick",
        universe="Earth-2",
        suit_color="Silver",
        enemies=["Shade", "Rival"]
    )
    print(f"\nAlternate Flash: {earth2_flash.display_info()}")
    print(f"Combat status: {earth2_flash._handle_enemy('Shade')}")