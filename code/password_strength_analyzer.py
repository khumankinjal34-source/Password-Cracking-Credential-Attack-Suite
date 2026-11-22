
import math
import string
import re


# Common passwords and predictable patterns
COMMON_PASSWORDS = {
    "123456",
    "password",
    "123456789",
    "qwerty",
    "admin",
    "password123",
    "hello123",
    "abc123",
    "letmein",
    "welcome",
    "iloveyou",
    "admin123",
}

KEYBOARD_PATTERNS = [
    "qwerty",
    "asdf",
    "zxcv",
    "12345",
    "09876",
    "qwert",
    "abcd",
]

COMMON_WORDS = [
    "password",
    "admin",
    "welcome",
    "student",
    "hello",
    "python",
    "login",
]


def calculate_entropy(password):
    """Calculate theoretical character-set entropy."""

    pool_size = 0

    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26

    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26

    if any(c in string.digits for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if any(c.isspace() for c in password):
        pool_size += 1

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def detect_patterns(password):
    """Detect common and predictable password patterns."""

    lower_password = password.lower()
    findings = []

    if lower_password in COMMON_PASSWORDS:
        findings.append("Password matches a common password.")

    for word in COMMON_WORDS:
        if word in lower_password:
            findings.append(
                f"Contains a predictable word: '{word}'."
            )
            break

    for pattern in KEYBOARD_PATTERNS:
        if pattern in lower_password:
            findings.append(
                f"Contains a predictable sequence: '{pattern}'."
            )
            break

    if re.search(r"(.)\1{2,}", password):
        findings.append(
            "Contains three or more repeated characters."
        )

    if re.search(r"0123|1234|2345|3456|4567|5678|6789", password):
        findings.append(
            "Contains a sequential number pattern."
        )

    if re.search(r"abcd|bcde|cdef|defg|efgh|fghi", lower_password):
        findings.append(
            "Contains a sequential alphabet pattern."
        )

    if re.search(r"(19|20)\d{2}", password):
        findings.append(
            "Contains a year-like number pattern."
        )

    return findings


def analyze_password(password):
    """Analyze password strength and return detailed results."""

    length = len(password)

    checks = {
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digits": any(c.isdigit() for c in password),
        "special": any(c in string.punctuation for c in password),
        "spaces": any(c.isspace() for c in password),
    }

    entropy = calculate_entropy(password)
    patterns = detect_patterns(password)

    score = 0
    recommendations = []

    # Length evaluation
    if length >= 8:
        score += 1
    else:
        recommendations.append("Use at least 12 characters.")

    if length >= 12:
        score += 1

    if length >= 16:
        score += 1

    # Character diversity
    for category, present in checks.items():
        if present:
            score += 1

    if not checks["lowercase"]:
        recommendations.append("Include lowercase letters.")

    if not checks["uppercase"]:
        recommendations.append("Include uppercase letters.")

    if not checks["digits"]:
        recommendations.append("Include numbers.")

    if not checks["special"]:
        recommendations.append("Include special characters.")

    # Predictability penalties
    if patterns:
        score -= min(len(patterns) * 2, 5)

    # Common passwords should never receive a strong rating
    if password.lower() in COMMON_PASSWORDS:
        score = 0

    score = max(0, min(score, 8))

    # Strength classification
    if patterns or length < 8:
        strength = "WEAK"
    elif score <= 3:
        strength = "WEAK"
    elif score <= 5:
        strength = "MODERATE"
    else:
        strength = "STRONG"

    # Additional recommendations
    if patterns:
        recommendations.append(
            "Avoid common words, keyboard patterns and predictable sequences."
        )

    if length < 12:
        recommendations.append(
            "Use a longer password or passphrase."
        )

    if not recommendations:
        recommendations.append(
            "No basic improvements detected. Still use a unique password."
        )

    return {
        "length": length,
        "checks": checks,
        "entropy": round(entropy, 2),
        "score": score,
        "strength": strength,
        "patterns": patterns,
        "recommendations": recommendations,
    }


def main():

    print("\n" + "=" * 48)
    print("       PASSWORD STRENGTH ANALYZER")
    print("=" * 48)

    password = input(
        "Enter a fictional test password (never use a real password): "
    )

    if not password:
        print("Error: Password cannot be empty.")
        return

    result = analyze_password(password)

    print("\nPASSWORD ANALYSIS")
    print("-" * 48)

    print("Length:", result["length"])
    print("Character checks:", result["checks"])

    print(
        "Estimated character-set entropy:",
        result["entropy"],
        "bits"
    )

    print("Score:", str(result["score"]) + "/8")
    print("Strength:", result["strength"])

    print("\nPREDICTABILITY CHECK")

    if result["patterns"]:
        for finding in result["patterns"]:
            print("-", finding)
    else:
        print("No basic predictable patterns detected.")

    print("\nRECOMMENDATIONS")

    for recommendation in result["recommendations"]:
        print("-", recommendation)

    print("\nNote:")
    print(
        "Entropy is a theoretical estimate, not a reliable "
        "measure of real-world password strength."
    )
    print(
        "This educational analyzer uses basic pattern checks "
        "and is not a professional password-cracking estimator."
    )

    print("=" * 48)


if __name__ == "__main__":
    main()
