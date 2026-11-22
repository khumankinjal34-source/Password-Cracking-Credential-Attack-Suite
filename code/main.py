"""Main menu for the Password Security Assessment Suite."""
from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent
MODULES = {
    "1": ("Password Strength Analyzer", "password_strength_analyzer.py"),
    "2": ("Dictionary Generator", "dictionary_generator.py"),
    "3": ("Hash Format Analyzer", "hash_analyzer.py"),
    "4": ("Brute-Force Simulator", "brute_force_simulator.py"),
    "5": ("Security Audit Report", "security_audit_report.py"),
}

def run_module(script_name):
    script_path = BASE_DIR / script_name
    if not script_path.is_file():
        print(f"Error: {script_name} was not found in {BASE_DIR}")
        return
    try:
        completed = subprocess.run([sys.executable, str(script_path)], cwd=BASE_DIR, check=False)
        if completed.returncode != 0:
            print(f"\nModule exited with status code {completed.returncode}.")
    except OSError as exc:
        print(f"Could not start module: {exc}")

def main():
    while True:
        print("\n" + "=" * 52)
        print("     PASSWORD SECURITY ASSESSMENT SUITE")
        print("=" * 52)
        for key, (label, _) in MODULES.items():
            print(f"{key}. {label}")
        print("6. Exit")
        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "6":
            print("Exiting toolkit. Thank you.")
            break
        if choice in MODULES:
            label, script = MODULES[choice]
            print(f"\nLaunching {label}...\n")
            run_module(script)
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
