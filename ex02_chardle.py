"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730886707"


def main() -> None:
    """The entry point of the program."""
    contains_char(word=input_word(), letter=input_letter())
    # The entry point of the program allowing us to call our input functions.


def input_word() -> str:
    """Collects a 5-character word from the user."""
    # We will use input() to get data from the user as a string.
    user_word: str = input("Enter a 5-character word: ")
    # This function will check the length of the word.
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # This function will let us exit early if the word is invalid.
    return user_word


def input_letter() -> str:
    """Collects a single character from the user"""
    user_char: str = input("Enter a single character: ")
    if len(user_char) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_char


def contains_char(word: str, letter: str) -> None:
    """Checks each index of the word for matches with the letter."""
    print("Searching for " + letter + " in " + word)

    # A Counting variable which stores amount of matches found.
    count: int = 0

    # These functions will check indices manually.
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1

    # This function will provide us with a final count.
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
