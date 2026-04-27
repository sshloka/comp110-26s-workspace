"""File to define Bear class."""


class Bear:
    """Bear in the river."""

    age: int
    hunger_score: int

    def __init__(self) -> None:
        """Initiatlize age and hunger_score to 0."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self) -> None:
        """Increase age by 1 and decrease hunger by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int) -> None:
        """Increase hunger_score by the amount of fish eaten."""
        self.hunger_score += num_fish
        return None
