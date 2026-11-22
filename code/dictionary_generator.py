
from pathlib import Path


# Educational variations for fictional test words only.
SUFFIXES = ["123", "2026", "!", "@", "123!"]
PREFIXES = ["!", "@"]

LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7"
}


def generate_variations(words):
    """Generate basic educational password variations."""

    variations = set()

    for word in words:
        word = word.strip()

        if not word:
            continue

        base_forms = {
            word,
            word.lower(),
            word.upper(),
            word.capitalize()
        }

        # Add basic leetspeak transformation
        leet_word = "".join(
            LEET_MAP.get(char.lower(), char)
            for char in word
        )

        base_forms.add(leet_word)

        for base in base_forms:
            variations.add(base)

            # Add suffix variations
            for suffix in SUFFIXES:
                variations.add(base + suffix)

            # Add prefix variations
            for prefix in PREFIXES:
                variations.add(prefix + base)

    return sorted(variations)


def save_wordlist(variations):
    """Save generated entries in the project's Data folder."""

    project_root = Path(__file__).resolve().parent.parent
    data_folder = project_root / "Data"

    data_folder.mkdir(parents=True, exist_ok=True)

    output_file = data_folder / "generated_wordlist.txt"

    with output_file.open("w", encoding="utf-8") as file:
        for word in variations:
            file.write(word + "\n")

    return output_file


def main():

    print("\n" + "=" * 48)
    print("       EDUCATIONAL DICTIONARY GENERATOR")
    print("=" * 48)

    print("Use fictional test words only.")
    print("Do not enter real names, birthdays or personal information.")

    user_input = input(
        "\nEnter comma-separated fictional test words: "
    )

    words = [
        word.strip()
        for word in user_input.split(",")
        if word.strip()
    ]

    if not words:
        print("Error: Please enter at least one test word.")
        return

    variations = generate_variations(words)

    if not variations:
        print("No valid entries generated.")
        return

    output_file = save_wordlist(variations)

    print("\nGENERATION SUMMARY")
    print("-" * 48)
    print("Original test words:", len(words))
    print("Unique generated entries:", len(variations))
    print("Output file:", output_file)

    print("\nFIRST 10 GENERATED ENTRIES")

    for word in variations[:10]:
        print("-", word)

    if len(variations) > 10:
        print("...")

    print("\nDictionary generation completed successfully.")
    print("These entries are for controlled educational testing only.")

    print("=" * 48)


if __name__ == "__main__":
    main()
