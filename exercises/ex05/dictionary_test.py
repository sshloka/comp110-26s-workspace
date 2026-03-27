"""EX06 - Dictionary Unit Tests - Practice with writing unit tests."""

__author__: str = "730886707"

import pytest
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance

# invert


def test_invert_basic() -> None:
    """Use case: invert a normal dictionary."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_single() -> None:
    """Use case: dictionary with one key-value pair."""
    assert invert({"x": "y"}) == {"y": "x"}


def test_invert_duplicate_values() -> None:
    """Edge case: duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "1", "b": "1"})


# favorite_color


def test_favorite_color_basic() -> None:
    """Use case: most frequent color."""
    assert favorite_color({"A": "blue", "B": "red", "C": "blue"}) == "blue"


def test_favorite_color_all_unique() -> None:
    """Use case: all colors unique (returns first encountered)."""
    assert favorite_color({"A": "blue", "B": "red", "C": "green"}) == "blue"


def test_favorite_color_empty() -> None:
    """Edge case: empty dictionary."""
    assert favorite_color({}) == ""


# count


def test_count_basic() -> None:
    """Use case: normal list with repeats."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_single_item() -> None:
    """Use case: list with one item."""
    assert count(["x"]) == {"x": 1}


def test_count_empty() -> None:
    """Edge case: empty list."""
    assert count([]) == {}


# alphabetizer


def test_alphabetizer_basic() -> None:
    """Use case: grouping words by first letter."""
    result = alphabetizer(["apple", "banana", "apricot"])
    assert result == {"a": ["apple", "apricot"], "b": ["banana"]}


def test_alphabetizer_mixed_case() -> None:
    """Use case: handles uppercase and lowercase."""
    result = alphabetizer(["Apple", "banana"])
    assert result == {"a": ["Apple"], "b": ["banana"]}


def test_alphabetizer_non_alpha() -> None:
    """Edge case: ignores non-alphabetic strings."""
    result = alphabetizer(["apple", "123", "banana!"])
    assert result == {"a": ["apple"]}


# update_attendance


def test_update_attendance_existing_day() -> None:
    """Use case: add student to existing day."""
    attendance = {"Monday": ["Alice"]}
    update_attendance(attendance, "Monday", "Bob")
    assert attendance == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_new_day() -> None:
    """Use case: add new day with student."""
    attendance = {}
    update_attendance(attendance, "Tuesday", "Alice")
    assert attendance == {"Tuesday": ["Alice"]}


def test_update_attendance_multiple_updates() -> None:
    """Edge: case: multiple updates to same day."""
    attendance = {"Wednesday": []}
    update_attendance(attendance, "Wednesday", "Alice")
    update_attendance(attendance, "Wednesday", "Bob")
    assert attendance == {"Wednesday": ["Alice", "Bob"]}
