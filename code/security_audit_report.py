
from datetime import datetime
from pathlib import Path

from password_strength_analyzer import analyze_password


def get_value(data, possible_keys, default=None):
    """Return the first matching value from an analysis dictionary."""
    for key in possible_keys:
        if key in data and data[key] is not None:
            return data[key]
    return default


def analyze_lab_password(password):
    """Analyze one fictional password without storing its actual value."""
    result = analyze_password(password)

    if not isinstance(result, dict):
        raise TypeError(
            "The analyzer must return a dictionary. "
            "Please check analyze_password() in password_strength_analyzer.py."
        )

    strength = get_value(
        result,
        ["strength", "level", "category", "classification"],
        "Not provided"
    )

    score = get_value(result, ["score", "strength_score"], "Not provided")

    entropy = get_value(
        result,
        ["entropy", "entropy_bits", "entropy_estimate"],
        "Not provided"
    )

    recommendations = get_value(
        result,
        ["recommendations", "feedback", "suggestions", "issues"],
        []
    )

    if isinstance(recommendations, str):
        recommendations = [recommendations]
    elif not isinstance(recommendations, (list, tuple)):
        recommendations = []

    return {
        "length": len(password),
        "strength": str(strength),
        "score": score,
        "entropy": entropy,
        "recommendations": [str(item) for item in recommendations]
    }


def create_report(results):
    """Create a text audit report from analysis results."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total = len(results)
    weak = sum("weak" in item["strength"].lower() for item in results)
    medium = sum(
        any(word in item["strength"].lower()
            for word in ["medium", "moderate", "fair"])
        for item in results
    )
    strong = sum("strong" in item["strength"].lower() for item in results)

    lines = [
        "=" * 60,
        "             PASSWORD SECURITY AUDIT REPORT",
        "=" * 60,
        "",
        f"Report generated: {now}",
        "Assessment type: Educational password policy assessment",
        "Scope: Fictional passwords supplied for local lab testing",
        "",
        "-" * 60,
        "1. AUDIT SUMMARY",
        "-" * 60,
        f"Total passwords analyzed: {total}",
        f"Weak passwords:           {weak}",
        f"Medium passwords:         {medium}",
        f"Strong passwords:         {strong}",
        "",
        "-" * 60,
        "2. INDIVIDUAL RESULTS",
        "-" * 60,
        "Actual password values are intentionally not included.",
        ""
    ]

    for index, item in enumerate(results, start=1):
        lines.extend([
            f"Test password #{index}",
            f"Length: {item['length']} characters",
            f"Strength: {item['strength']}",
            f"Score: {item['score']}",
            f"Estimated entropy: {item['entropy']}",
            "Recommendations:"
        ])

        if item["recommendations"]:
            for recommendation in item["recommendations"]:
                lines.append(f"  - {recommendation}")
        else:
            lines.append("  - Follow the organization's password policy.")

        lines.append("")

    lines.extend([
        "-" * 60,
        "3. SECURITY RECOMMENDATIONS",
        "-" * 60,
        "1. Use long, unique passwords for every account.",
        "2. Avoid common words, predictable patterns, and reused passwords.",
        "3. Use a password manager to create and store unique passwords.",
        "4. Enable multi-factor authentication wherever possible.",
        "5. Apply rate limiting and account protection against repeated login attempts.",
        "6. Encourage users to use passphrases or randomly generated passwords.",
        "",
        "-" * 60,
        "4. SCOPE AND LIMITATIONS",
        "-" * 60,
        "- This report is based only on fictional lab password inputs.",
        "- No real user accounts or credentials were accessed.",
        "- Strength ratings are estimates from the local analyzer.",
        "- Entropy estimates do not guarantee resistance to real attacks.",
        "- This report does not represent a live system security assessment.",
        "",
        "=" * 60,
        "                 END OF AUDIT REPORT",
        "=" * 60
    ])

    return "\n".join(lines)


def main():
    print("=" * 60)
    print("              SECURITY AUDIT REPORT")
    print("=" * 60)
    print("Educational assessment using fictional passwords only.")
    print()
    print("Enter fictional lab passwords separated by commas.")
    print("Example: Password123!,hello123,Test@123")
    print()

    user_input = input("Enter lab passwords: ").strip()

    passwords = [
        password.strip()
        for password in user_input.split(",")
        if password.strip()
    ]

    if not passwords:
        print("Error: Please enter at least one password.")
        return

    print()
    print("Analyzing passwords...")

    results = []

    try:
        for index, password in enumerate(passwords, start=1):
            result = analyze_lab_password(password)
            results.append(result)

            print(
                f"Password #{index}: "
                f"{result['strength']} "
                f"(Length: {result['length']})"
            )

    except Exception as error:
        print(f"\nAudit could not be completed: {error}")
        return

    report_text = create_report(results)

    project_root = Path(__file__).resolve().parent.parent
    reports_folder = project_root / "reports"
    reports_folder.mkdir(parents=True, exist_ok=True)

    report_file = reports_folder / "security_audit_report.txt"

    try:
        report_file.write_text(report_text, encoding="utf-8")
    except OSError as error:
        print(f"\nCould not save report: {error}")
        return

    print()
    print("-" * 60)
    print("AUDIT SUMMARY")
    print("-" * 60)

    weak = sum("weak" in item["strength"].lower() for item in results)
    strong = sum("strong" in item["strength"].lower() for item in results)

    print(f"Total analyzed: {len(results)}")
    print(f"Weak passwords: {weak}")
    print(f"Strong passwords: {strong}")
    print()
    print("Audit completed successfully!")
    print(f"Report saved to: {report_file}")


if __name__ == "__main__":
    main()
