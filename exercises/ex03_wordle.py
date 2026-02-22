"""EX03 - Wordle. A word guessing game!"""

__author__: str = "730886707"

# Emoji constants (named constants improve readability)
WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6
    won: bool = False

    # Game loop continues while player has turns remaining and hasn't won
    while turn <= max_turns and not won:
        print(f"=== Turn {turn}/{max_turns} ===")
        guess: str = input_guess(len(secret))
        emoji_result: str = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            won = True
        else:
            turn += 1

    # After game loop ends, print result message
    if won:
        print(f"You won in {turn}/{max_turns} turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def input_guess(secret_word_len: int) -> str:
    """Ask the user for a guess of the word's length."""
    guess: str = input(f"Enter a {secret_word_len} character word: ")

    # Keep asking until the user provides the correct length
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if char_guess is contained anywhere in secret_word."""
    assert len(char_guess) == 1
    idx: int = 0

    # Mannually check each character in secret_word
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Return emoji string representing accuracy of guess vs. secret."""
    assert len(guess) == len(secret)

    idx: int = 0
    result: str = ""

    # Compare each character position
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        else:
            # Use contains_char to check for yellow boxes
            if contains_char(secret, guess[idx]):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        idx += 1
    return result


if __name__ == "__main__":
    main(secret="codes")
