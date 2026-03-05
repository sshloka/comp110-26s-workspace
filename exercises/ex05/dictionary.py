"""EX05 - Dictionary Utility Functions. Practice with dictionary functions."""

__author__: str = "730886707"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Return a dictionary with keys and values inverted."""
    result: dict[str, str] = {}

    for key in input_dict:
        value = input_dict[key]
        if value in result:
            raise KeyError("Duplicate key when inverting dictionary.")
        result[value] = key

    return result


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most frequent favorite color."""
    color_counts: dict[str, int] = {}
    most_popular: str = ""
    highest_count: int = 0

    for name in colors:
        color = colors[name]

        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

        if color_counts[color] > highest_count:
            highest_count = color_counts[color]
            most_popular = color

    return most_popular


def count(values: list[str]) -> dict[str, int]:
    """Count frequency of each string in a list."""
    result: dict[str, int] = {}

    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1

    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their starting letter."""
    result: dict[str, list[str]] = {}

    for word in words:
        if word.isalpha():
            first_letter = word[0].lower()

            if first_letter in result:
                result[first_letter].append(word)
            else:
                result[first_letter] = [word]

    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance log with a student for a given day."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]
