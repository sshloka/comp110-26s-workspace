"""EX08 - Linked List Utils - Processing a singly-linked list data structure."""

from __future__ import annotations

__author__: str = "730886707"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a new Node object."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Provide a string representation for printing."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return the value of the Node at the given index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    elif index == 0:
        return head.value
    else:
        return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Returns the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    elif head.next is None:
        return head.value
    else:
        rest_max = max(head.next)
        if head.value > rest_max:
            return head.value
        else:
            return rest_max


def linkify(items: list[int]) -> Node | None:
    """Converts a Python list of integers into a linked list of Nodes."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a new linked list where each value is multiplied by factor."""
    if head is None:
        return None
    new_val = head.value * factor

    return Node(new_val, scale(head.next, factor))


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)
