
import hashlib
import re


# Supported demonstration hash formats
HASH_FORMATS = {
    32: "MD5 candidate",
    40: "SHA-1 candidate",
    64: "SHA-256 candidate",
    128: "SHA-512 candidate"
}


def generate_hash(password, algorithm):
    """Generate an example hash from a fictional test string."""

    algorithms = {
        "md5": hashlib.md5,
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }

    if algorithm not in algorithms:
        raise ValueError("Unsupported hash algorithm.")

    return algorithms[algorithm](
        password.encode("utf-8")
    ).hexdigest()


def identify_hash(hash_value):
    """Identify possible hash formats by hexadecimal length."""

    hash_value = hash_value.strip()

    if not hash_value:
        return "Empty input"

    if not re.fullmatch(r"[0-9a-fA-F]+", hash_value):
        return "Invalid hash: hexadecimal characters expected"

    # NTLM is commonly represented as a 32-character
    # hexadecimal value, so length alone cannot distinguish it.
    if len(hash_value) == 32:
        return "MD5 or NTLM candidate (length alone is inconclusive)"

    return HASH_FORMATS.get(
        len(hash_value),
        "Unknown or unsupported hash format"
    )


def parse_synthetic_shadow(line):
    """
    Parse a fictional Linux shadow-style entry.
    This does not access /etc/shadow.
    """

    fields = line.strip().split(":")

    if len(fields) != 9:
        raise ValueError(
            "Expected exactly 9 colon-separated fields."
        )

    username = fields[0]
    password_field = fields[1]

    if not username:
        raise ValueError("Username field cannot be empty.")

    if password_field.startswith("$6$"):
        algorithm = "SHA-512 crypt-style candidate"
    elif password_field.startswith("$5$"):
        algorithm = "SHA-256 crypt-style candidate"
    elif password_field.startswith("$1$"):
        algorithm = "MD5 crypt-style candidate"
    elif password_field in ("!", "*", "!!"):
        algorithm = "Locked or unavailable password field"
    elif password_field.startswith("$"):
        algorithm = "Other modular crypt format"
    else:
        algorithm = "Unrecognized or locked password field"

    return {
        "username": username,
        "algorithm": algorithm,
        "last_change": fields[2],
        "minimum_age": fields[3],
        "maximum_age": fields[4],
        "warning_period": fields[5]
    }


def inspect_ntlm(value):
    """
    Inspect the shape of a fictional NTLM-style value.
    Does not crack or verify credentials.
    """

    value = value.strip()

    if not re.fullmatch(r"[0-9a-fA-F]{32}", value):
        raise ValueError(
            "Expected exactly 32 hexadecimal characters."
        )

    return (
        "Valid 32-character hexadecimal shape. "
        "NTLM candidate, but MD5 cannot be excluded by length alone."
    )


def main():

    while True:

        print("\n" + "=" * 48)
        print("             HASH FORMAT ANALYZER")
        print("=" * 48)

        print("1. Generate example hashes")
        print("2. Identify a hash string")
        print("3. Parse a synthetic Linux shadow-style line")
        print("4. Inspect a synthetic Windows NTLM-shaped value")
        print("5. Exit")

        choice = input("Choose 1-5: ").strip()

        if choice == "1":

            password = input(
                "Enter a fictional test string: "
            )

            if not password:
                print("Error: Input cannot be empty.")
                continue

            print("\nGENERATED HASHES")

            for algorithm in ("md5", "sha1", "sha256", "sha512"):
                result = generate_hash(password, algorithm)
                print(f"{algorithm.upper()}: {result}")

        elif choice == "2":

            value = input("Paste a hash string: ")
            print("Format:", identify_hash(value))

        elif choice == "3":

            print("\nUse this fictional example:")
            print("demo:$6$salt$samplehash:20000:0:99999:7:::")

            line = input(
                "\nEnter a synthetic shadow-style line: "
            )

            try:
                result = parse_synthetic_shadow(line)

                print("\nSYNTHETIC ENTRY ANALYSIS")

                for key, value in result.items():
                    print(f"{key}: {value}")

            except ValueError as error:
                print("Error:", error)

        elif choice == "4":

            print("\nUse a fictional 32-character hexadecimal value.")
            value = input("Enter test value: ")

            try:
                result = inspect_ntlm(value)
                print("\nFORMAT ANALYSIS")
                print(result)

            except ValueError as error:
                print("Error:", error)

        elif choice == "5":

            print("Exiting Hash Format Analyzer.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

        print(
            "\nSafety note: Synthetic examples only. "
            "No real credential files are accessed."
        )


if __name__ == "__main__":
    main()
