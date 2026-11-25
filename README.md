# 🔐 Password Cracking & Credential Attack Suite

<p align="center">
  <strong>An Educational Platform for Password Security Assessment</strong>
</p>

<p align="center">
  Python · Streamlit · Cybersecurity · Security Awareness
</p>

---

## 📌 Project Overview

The **Password Cracking & Credential Attack Suite** is an educational cybersecurity project developed to demonstrate password security concepts, analyze password strength, identify hash formats, simulate limited password-guessing scenarios, and generate security audit reports.

The project provides an interactive Streamlit dashboard with five modules that help learners understand common password vulnerabilities and explore defensive security practices in a controlled environment.

**Educational use only:** This application uses fictional test data and restricted simulations. It is not designed to extract real operating-system credentials or attack live accounts and services.

## 🚀 Live Application

**Try the application:**  
[Launch Password Security Assessment Suite](https://password-cracking-credential-attack-suite-lva3ycadeedl4yahob7d.streamlit.app/)

## ✨ Key Features

### 1. Password Strength Analyzer
- Evaluates password length and character variety.
- Estimates password entropy.
- Identifies predictable patterns.
- Provides security recommendations.

### 2. Dictionary Generator
- Generates password variations from fictional base words.
- Demonstrates common password-pattern variations.
- Produces a sample wordlist for educational testing.

### 3. Hash Format Analyzer
- Generates example MD5, SHA-1, SHA-256, and SHA-512 hashes.
- Identifies possible hash formats.
- Demonstrates synthetic Linux shadow-style entries.
- Inspects NTLM-shaped sample values.

### 4. Brute-Force Simulator
- Demonstrates a restricted brute-force simulation.
- Uses small educational character sets.
- Limits the maximum simulated password length.
- Displays attempts, elapsed time, and search-space information.

### 5. Security Audit Report
- Evaluates multiple fictional passwords.
- Summarizes password-strength findings.
- Provides security recommendations.
- Generates an audit-style report without exposing the submitted password values.

## 🛠️ Technologies Used

- **Python** – Application logic and security analysis.
- **Streamlit** – Interactive web application interface.
- **Hashlib** – Example cryptographic hash generation.
- **Git & GitHub** – Version control and project hosting.

## 📂 Project Structure

```text
Password-Cracking-Credential-Attack-Suite/
│
├── code/
│   ├── brute_force_simulator.py
│   ├── dictionary_generator.py
│   ├── hash_analyzer.py
│   ├── main.py
│   ├── password_strength_analyzer.py
│   ├── security_audit_report.py
│   └── code.zip
│
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.10 or later
- Git
- Visual Studio Code (recommended)

### 1. Clone the repository

```bash
git clone https://github.com/khumankinjal34-source/Password-Cracking-Credential-Attack-Suite.git
```

### 2. Open the project directory

```bash
cd Password-Cracking-Credential-Attack-Suite
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run streamlit_app.py
```

The application will open in your default browser.

## 🧪 Testing & Demonstration

The project includes five educational modules that can be tested independently through the Streamlit interface.

Testing focuses on:
- Password-strength evaluation.
- Dictionary variation generation.
- Example hash generation and format identification.
- Restricted brute-force simulation.
- Security audit report generation.

Use fictional passwords and sample data only.

## 🔒 Security & Ethical Considerations

This project is intended for educational demonstrations and controlled security learning.

**Important limitations:**
- It does not extract real credentials from Windows SAM/SYSTEM files or Linux `/etc/shadow`.
- It does not connect to external login pages or network services.
- It does not perform real-world credential attacks.
- Brute-force functionality is restricted to a small educational simulation.
- Hash identification based on format alone may be inconclusive.

**Never enter real passwords, personal credentials, or sensitive authentication information into this application.**

## 🔮 Future Improvements

- Expand automated unit testing.
- Improve visualizations and reporting.
- Add more password-policy analysis options.
- Improve documentation and user guidance.
- Explore additional defensive security assessment features.

## 👨‍💻 Author

**Kinjal Khuman**

Python Developer | Cybersecurity Enthusiast

GitHub: [@khumankinjal34-source](https://github.com/khumankinjal34-source)

## 📄 License

No license has been added yet. All rights are reserved unless a license is added to this repository.

---

<p align="center">
  <strong>Built for Learning • Designed for Security Awareness</strong>
</p>
