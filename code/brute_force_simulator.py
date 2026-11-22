
import itertools
import string
import time


# Small educational character sets
CHARACTER_SETS = {
    "1": {
        "name": "Lowercase letters",
        "characters": string.ascii_lowercase
    },
    "2": {
        "name": "Lowercase + digits",
        "characters": string.ascii_lowercase + string.digits
    },
    "3": {
        "name": "Small lab set",
        "characters": "abc123"
    }
}

MAX_ALLOWED_LENGTH = 4


def calculate_search_space(charset_size, max_length):
    """Calculate the total number of possible combinations."""

    total = 0

    for length in range(1, max_length + 1):
        total += charset_size ** length

    return total


def format_time(seconds):
    """Convert seconds into a readable time."""

    if seconds < 1:
        return f"{seconds:.8f} seconds"

    if seconds < 60:
        return f"{seconds:.2f} seconds"

    if seconds < 3600:
        return f"{seconds / 60:.2f} minutes"

    if seconds < 86400:
        return f"{seconds / 3600:.2f} hours"

    if seconds < 31536000:
        return f"{seconds / 86400:.2f} days"

    years = seconds / 31536000

    return f"{years:.2f} years"


def simulate_guessing(test_password, characters, max_length):
    """
    Simulate guesses against a fictional lab password.

    Only small character sets and lengths are allowed.
    """

    attempts = 0
    start_time = time.perf_counter()

    for length in range(1, max_length + 1):

        for combination in itertools.product(
            characters, repeat=length
        ):

            attempts += 1
            guess = "".join(combination)

            if guess == test_password:

                elapsed = time.perf_counter() - start_time

                return {
                    "found": True,
                    "attempts": attempts,
                    "elapsed": elapsed,
                    "password_length": length
                }

    elapsed = time.perf_counter() - start_time

    return {
        "found": False,
        "attempts": attempts,
        "elapsed": elapsed,
        "password_length": None
    }


def main():

    print("\n" + "=" * 48)
    print("          BRUTE-FORCE SIMULATOR")
    print("=" * 48)

    print("Educational simulation using fictional passwords only.")

    print("\nAVAILABLE CHARACTER SETS")

    for key, value in CHARACTER_SETS.items():
        print(f"{key}. {value['name']}")

    choice = input("\nChoose character set (1-3): ").strip()

    if choice not in CHARACTER_SETS:
        print("Error: Please select a valid character set.")
        return

    selected = CHARACTER_SETS[choice]
    characters = selected["characters"]

    try:
        max_length = int(
            input("Maximum test length (1-4): ").strip()
        )

        if not 1 <= max_length <= MAX_ALLOWED_LENGTH:
            print("Error: Maximum length must be between 1 and 4.")
            return

    except ValueError:
        print("Error: Enter a whole number from 1 to 4.")
        return

    test_password = input(
        "Enter a fictional lab password: "
    )

    if not test_password:
        print("Error: Password cannot be empty.")
        return

    if len(test_password) > max_length:
        print("Error: Password is longer than the selected maximum length.")
        return

    if any(char not in characters for char in test_password):
        print("Error: Password contains characters outside the selected set.")
        return

    # Calculate theoretical search space
    search_space = calculate_search_space(
        len(characters),
        max_length
    )

    print("\nSIMULATION CONFIGURATION")
    print("-" * 48)
    print("Character set:", selected["name"])
    print("Character count:", len(characters))
    print("Maximum length:", max_length)
    print("Total possible combinations:", search_space)

    print("\nRunning educational simulation...")

    result = simulate_guessing(
        test_password,
        characters,
        max_length
    )

    print("\nSIMULATION RESULTS")
    print("-" * 48)

    print("Password found:", "Yes" if result["found"] else "No")
    print("Attempts performed:", result["attempts"])
    print("Actual elapsed time:", format_time(result["elapsed"]))

    # Theoretical estimate based on measured attempt rate.
    if result["elapsed"] > 0 and result["attempts"] > 0:

        attempts_per_second = (
            result["attempts"] / result["elapsed"]
        )

        estimated_full_search_time = (
            search_space / attempts_per_second
        )

        print(
            "Measured simulation rate:",
            f"{attempts_per_second:.2f} attempts/second"
        )

        print(
            "Theoretical full-search estimate:",
            format_time(estimated_full_search_time)
        )

    else:
        print(
            "Theoretical time estimate unavailable "
            "because the measured duration was too short."
        )

    if result["found"]:
        print(
            "Matched password length:",
            result["password_length"]
        )

    print("\nSECURITY NOTE")
    print(
        "This is a small educational simulation, "
        "not a real-world password cracking tool."
    )
    print(
        "Time estimates are approximate and depend "
        "on the local computer and implementation."
    )

    print("=" * 48)


if __name__ == "__main__":
    main()
