"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__: str = "730886707"


class River:
    """An ecosystem simulation of bears and fish."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Construct a river with fish and bears."""
        self.day = 0
        self.fish = []
        self.bears = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Remove animals that have passed their maximum age."""
        new_fish: list[Fish] = []
        for f in self.fish:
            if f.age <= 3:
                new_fish.append(f)
        self.fish = new_fish

        new_bears: list[Bear] = []
        for b in self.bears:
            if b.age <= 5:
                new_bears.append(b)
        self.bears = new_bears

        return None

    def remove_fish(self, amount: int) -> None:
        """Remove fish from the front of the list."""
        for _ in range(amount):
            if len(self.fish) > 0:
                self.fish.pop(0)
        return None

    def bears_eating(self) -> None:
        """Bears eat 3 fish if the population is at least 5."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self) -> None:
        """Remove bears that have a hunger score below 0."""
        surviving_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self) -> None:
        """Each pair of fish produces 4 offspring."""
        n: int = len(self.fish)
        for _ in range((n // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self) -> None:
        """Each pair of bears produces 1 offspring."""
        n: int = len(self.bears)
        for _ in range(n // 2):
            self.bears.append(Bear())
        return None

    def __str__(self) -> str:
        """Return status of the river."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """Combine two rivers."""
        return River(
            len(self.fish) + len(other_riv.fish), len(self.bears) + len(other_riv.bears)
        )

    def __mul__(self, factor: int) -> River:
        """Multiply river populations."""
        return River(len(self.fish) * factor, len(self.bears) * factor)

    def one_river_day(self) -> None:
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)
        return None

    def one_river_week(self) -> None:
        """Simulate seven days."""
        for _ in range(7):
            self.one_river_day()
