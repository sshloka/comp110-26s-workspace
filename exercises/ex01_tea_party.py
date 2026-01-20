"""Ex01 is a function which uses guests to calculate tea bags, treats, and cost."""

__author__: str = "730886707"


def main_planner(guests: int) -> None:
    """Function that brings all of the below functions together."""
    tea_count = tea_bags(people=guests)
    treat_count = treats(people=guests)
    total_cost = cost(tea_count, treat_count)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(total_cost))


def tea_bags(people: int) -> int:
    """Function that calculates tea bags needed based on guests attending."""
    return people * 2


def treats(people: int) -> int:
    """Function that computes the number of treats needed."""
    teas = tea_bags(people=people)
    treats = teas * 1.5
    return int(treats)


def cost(tea_count: int, treat_count: int) -> float:
    """Function that computes the cost of both the tea bags and the treats."""
    cost = (tea_count * 0.50) + (treat_count * 0.75)
    return cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
