"""Ex01 is a function which uses guests to calculate tea bags, treats, and cost."""

__author__: str = "730886707"


def main_planner(guests: int) -> None:
    """Entrypoint Function of the Program."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Function that calculates tea bags needed based on guests attending."""
    return people * 2


def treats(people: int) -> int:
    """Function that computes the number of treats needed."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Function that computes the cost of both the tea bags and the treats."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
