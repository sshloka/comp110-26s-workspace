"""File to define Fish class."""


class Fish:
    """Fish living in the river."""

    age: int

    def __init__(self) -> None:
        """Initialize age to 0."""
        self.age = 0
        return None

    def one_day(self) -> None:
        """Increase age by 1."""
        self.age += 1
        return None
