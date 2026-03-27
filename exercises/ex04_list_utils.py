"""EX04 - List Utility Functions. Understanding and intentionally reproducing code."""

__author__: str = "730886707"


def all(input: list[int], value: int) -> bool:
    """Return True if all elements in input equal value. Return False if otherwise."""
    if len(input) == 0:
        return False

    for item in input:
        if item != value:
            return False

    return True


def max(input: list[int]) -> int:
    """Return the largest integer in the list. Raise ValueError if the list is empty."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest: int = input[0]

    for item in input:
        if item > largest:
            largest = item

    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Return True if both lists contain equal elements in the same order."""
    if len(list1) != len(list2):
        return False

    index: int = 0
    for item in list1:
        if item != list2[index]:
            return False
        index += 1

    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Mutate list1 by appending all elements of list2 to it."""
    for item in list2:
        list1.append(item)
