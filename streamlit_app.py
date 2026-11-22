import sys
from pathlib import Path

import streamlit as st

# --------------------------------------------------
# PROJECT PATHS AND MODULE IMPORTS
# --------------------------------------------------

PROJECT_DIR = Path(__file__).resolve().parent
CODE_DIR = PROJECT_DIR / "code"
DATA_DIR = PROJECT_DIR / "Data"
REPORTS_DIR = PROJECT_DIR / "reports"

# Make the existing project modules available to this Streamlit app.
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from password_strength_analyzer import analyze_password
from dictionary_generator import generate_variations, save_wordlist
from hash_analyzer import (
    generate_hash,
    identify_hash,
    parse_synthetic_shadow,
    inspect_ntlm,
)
from brute_force_simulator import (
    CHARACTER_SETS,
    MAX_ALLOWED_LENGTH,
    calculate_search_space,
    simulate_guessing,
    format_time,
)
from security_audit_report import analyze_lab_password, create_report


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Password Security Assessment Suite",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)


# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown(
    """
    <style>
        .stApp {
            background-color: #0e1117;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .dashboard-title {
            font-size: 34px;
            font-weight: 750;
            color: #ffffff;
            margin-bottom: 5px;
        }

        .dashboard-subtitle {
            color: #aab4c3;
            font-size: 15px;
            margin-bottom: 25px;
        }

        .security-card {
            background-color: #1b2433;
            border: 1px solid #344155;
            padding: 20px;
            border-radius: 12px;
            min-height: 125px;
            margin-bottom: 12px;
        }

        .security-card h3 {
            color: #ffffff;
            font-size: 17px;
        }

        .security-card p {
            color: #aab4c3;
            font-size: 13px;
        }

        section[data-testid="stSidebar"] {
            background-color: #151b27;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:
    st.title("🔐 Security Suite")
    st.caption("Educational Security Assessment")
    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Dashboard",
            "Password Strength Analyzer",
            "Dictionary Generator",
            "Hash Format Analyzer",
            "Brute-Force Simulator",
            "Security Audit Report",
        ],
    )

    st.divider()
    st.caption("PROJECT INFORMATION")
    st.write("Python + Streamlit")
    st.write("Educational laboratory")
    st.write("Fictional test data only")
    st.divider()
    st.caption("Password Security Assessment Suite")


# --------------------------------------------------
# COMMON HEADER
# --------------------------------------------------

st.markdown(
    '<div class="dashboard-title">🔐 Password Security Assessment Suite</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="dashboard-subtitle">'
    "A practical educational platform for password policy testing "
    "and credential security assessment."
    "</div>",
    unsafe_allow_html=True,
)


# --------------------------------------------------
# DASHBOARD HOME
# --------------------------------------------------

if page == "Dashboard":

    st.subheader("Welcome to the Security Dashboard")

    st.success("Your Password Security Assessment Suite is ready.")

    st.info(
        "This platform uses fictional passwords and synthetic "
        "examples for controlled educational testing only."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Available Modules", "5")

    with col2:
        st.metric("Application", "Ready")

    with col3:
        st.metric("Environment", "Educational")

    st.divider()
    st.subheader("Available Security Modules")

    modules = [
        (
            "🔑 Password Strength Analyzer",
            "Evaluate password length, character diversity, "
            "predictable patterns and estimated entropy.",
        ),
        (
            "📚 Dictionary Generator",
            "Generate basic variations from fictional laboratory words.",
        ),
        (
            "#️⃣ Hash Format Analyzer",
            "Generate demonstration hashes and identify possible formats.",
        ),
        (
            "🧪 Brute-Force Simulator",
            "Run a small offline simulation using restricted character sets.",
        ),
        (
            "📋 Security Audit Report",
            "Analyze fictional test passwords and generate a security report.",
        ),
    ]

    for module_title, description in modules:
        st.markdown(
            f"""
            <div class="security-card">
                <h3>{module_title}</h3>
                <p>{description}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.subheader("Security Notice")
    st.warning(
        "Never enter real account passwords, Windows credentials, "
        "personal information or production system credentials. "
        "Use fictional test data only."
    )


# --------------------------------------------------
# MODULE 1: PASSWORD STRENGTH ANALYZER
# --------------------------------------------------

elif page == "Password Strength Analyzer":

    st.subheader("🔑 Password Strength Analyzer")

    st.write(
        "Evaluate a fictional test password using the project's "
        "existing password analysis algorithm."
    )

    password = st.text_input(
        "Enter a fictional test password",
        type="password",
        help="Never enter a real account password.",
        key="strength_test_password",
    )

    if st.button("Analyze Password", type="primary"):

        if not password:
            st.error("Please enter a fictional test password.")

        else:
            result = analyze_password(password)

            st.divider()
            st.subheader("Analysis Results")

            col1, col2, col3 = st.columns(3)
            col1.metric("Password Length", result["length"])
            col2.metric("Security Score", f'{result["score"]}/8')
            col3.metric(
                "Estimated Entropy",
                f'{result["entropy"]} bits',
            )

            strength = result["strength"]

            if strength == "STRONG":
                st.success(f"Strength Classification: {strength}")
            elif strength == "MODERATE":
                st.warning(f"Strength Classification: {strength}")
            else:
                st.error(f"Strength Classification: {strength}")

            st.subheader("Character Checks")

            for category, present in result["checks"].items():
                if present:
                    st.write(f"✅ {category.capitalize()}")
                else:
                    st.write(f"❌ {category.capitalize()}")

            st.subheader("Predictability Findings")

            if result["patterns"]:
                for finding in result["patterns"]:
                    st.warning(finding)
            else:
                st.success("No basic predictable patterns detected.")

            st.subheader("Recommendations")

            for recommendation in result["recommendations"]:
                st.write(f"• {recommendation}")

            st.caption(
                "Entropy is a theoretical character-set estimate, "
                "not a guarantee of real-world password security."
            )
            st.caption(
                "The entered test value is not written to a report "
                "or saved by this application."
            )


# --------------------------------------------------
# MODULE 2: DICTIONARY GENERATOR
# --------------------------------------------------

elif page == "Dictionary Generator":

    st.subheader("📚 Dictionary Generator")

    st.write(
        "Generate basic word variations using fictional "
        "laboratory words."
    )

    base_words = st.text_area(
        "Enter fictional base words (one word per line)",
        placeholder="Example:\napple\nhello\npython",
        key="dictionary_base_words",
    )

    st.warning(
        "Use fictional words only. Do not enter personal information "
        "or real account passwords."
    )

    if st.button("Generate Wordlist", type="primary"):

        words = [
            word.strip()
            for word in base_words.splitlines()
            if word.strip()
        ]

        if not words:
            st.warning("Please enter at least one base word.")

        else:
            variations = generate_variations(words)

            st.success(
                f"Generated {len(variations)} unique wordlist entries."
            )

            st.download_button(
                label="Download Generated Wordlist",
                data="\n".join(variations),
                file_name="generated_wordlist.txt",
                mime="text/plain",
            )

            output_file = save_wordlist(variations)
            st.success(f"Wordlist saved to: {output_file}")


# --------------------------------------------------
# MODULE 3: HASH FORMAT ANALYZER
# --------------------------------------------------

elif page == "Hash Format Analyzer":

    st.subheader("#️⃣ Hash Format Analyzer")

    st.write(
        "Generate example hashes, identify possible hash formats "
        "and inspect synthetic credential-format demonstrations."
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Hash Generation",
            "Hash Identification",
            "Synthetic Shadow Demo",
            "NTLM Shape Demo",
        ]
    )

    with tab1:
        st.write("Generate example hashes from a fictional test string.")

        test_string = st.text_input(
            "Fictional test string",
            type="password",
            key="hash_test_string",
        )

        if st.button("Generate Example Hashes", key="generate_hashes"):

            if not test_string:
                st.error("Enter a fictional test string.")

            else:
                for algorithm in ["md5", "sha1", "sha256", "sha512"]:
                    value = generate_hash(test_string, algorithm)
                    st.write(f"**{algorithm.upper()}**")
                    st.code(value)

    with tab2:
        hash_value = st.text_input(
            "Enter a demonstration hash value",
            key="identify_hash_input",
        )

        if st.button("Identify Hash Format"):

            if not hash_value.strip():
                st.error("Please enter a hash value.")

            else:
                identification = identify_hash(hash_value)
                st.info(identification)

    with tab3:
        st.write("Use fictional Linux shadow-style data only.")

        st.code("demo:$6$salt$samplehash:20000:0:99999:7:::")

        shadow_line = st.text_input(
            "Synthetic shadow-style entry",
            value="demo:$6$salt$samplehash:20000:0:99999:7:::",
            key="synthetic_shadow_entry",
        )

        if st.button("Analyze Synthetic Entry"):

            try:
                result = parse_synthetic_shadow(shadow_line)

                for key, value in result.items():
                    st.write(
                        f"**{key.replace('_', ' ').title()}:** {value}"
                    )

            except ValueError as error:
                st.error(str(error))

    with tab4:
        st.write(
            "Inspect a fictional 32-character hexadecimal value. "
            "This does not crack or verify credentials."
        )

        ntlm_value = st.text_input(
            "Fictional NTLM-shaped test value",
            key="ntlm_test_value",
        )

        if st.button("Inspect NTLM Format"):

            try:
                result = inspect_ntlm(ntlm_value)
                st.success(result)

            except ValueError as error:
                st.error(str(error))

    st.caption(
        "Hash identification by length is inconclusive in some cases. "
        "For example, MD5 and NTLM can both have 32 hexadecimal characters."
    )


# --------------------------------------------------
# MODULE 4: BRUTE-FORCE SIMULATOR
# --------------------------------------------------

elif page == "Brute-Force Simulator":

    st.subheader("🧪 Brute-Force Simulator")

    st.warning(
        "Restricted offline educational simulation. "
        "Use fictional test strings only. Maximum test length is four."
    )

    selected_choice = st.selectbox(
        "Choose Character Set",
        options=list(CHARACTER_SETS.keys()),
        format_func=lambda key: CHARACTER_SETS[key]["name"],
    )

    selected = CHARACTER_SETS[selected_choice]
    characters = selected["characters"]

    st.write(f"**Character count:** {len(characters)}")
    st.code(characters)

    max_length = st.slider(
        "Maximum Test Length",
        min_value=1,
        max_value=MAX_ALLOWED_LENGTH,
        value=2,
    )

    test_password = st.text_input(
        "Fictional lab password",
        type="password",
        key="brute_force_test_password",
    )

    if st.button("Run Educational Simulation", type="primary"):

        if not test_password:
            st.error("Enter a fictional test password.")

        elif len(test_password) > max_length:
            st.error(
                "Password is longer than the selected maximum length."
            )

        elif any(char not in characters for char in test_password):
            st.error(
                "Password contains characters outside the selected set."
            )

        else:
            search_space = calculate_search_space(
                len(characters),
                max_length,
            )

            result = simulate_guessing(
                test_password,
                characters,
                max_length,
            )

            st.divider()
            st.subheader("Simulation Results")

            col1, col2, col3 = st.columns(3)
            col1.metric("Search Space", f"{search_space:,}")
            col2.metric("Attempts", f'{result["attempts"]:,}')
            col3.metric(
                "Elapsed Time",
                format_time(result["elapsed"]),
            )

            if result["found"]:
                st.success("Fictional test value matched!")
            else:
                st.error("Test value was not found.")

            if result["elapsed"] > 0 and result["attempts"] > 0:
                rate = result["attempts"] / result["elapsed"]
                estimated_time = search_space / rate

                st.write(
                    f"**Measured simulation rate:** "
                    f"{rate:.2f} attempts/second"
                )
                st.write(
                    "**Theoretical full-search estimate:** "
                    + format_time(estimated_time)
                )

            if result["found"]:
                st.write(
                    f'**Matched length:** {result["password_length"]}'
                )

            st.caption(
                "Theoretical estimates are based on this local simulation. "
                "They do not represent real-world cracking performance."
            )
            st.caption(
                "The fictional test value is not displayed in the results "
                "or saved to a report."
            )


# --------------------------------------------------
# MODULE 5: SECURITY AUDIT REPORT
# --------------------------------------------------

elif page == "Security Audit Report":

    st.subheader("📋 Security Audit Report")

    st.write(
        "Analyze multiple fictional laboratory passwords and "
        "generate a security assessment report."
    )

    user_input = st.text_area(
        "Enter fictional test passwords separated by commas",
        placeholder="Example: Password123!, hello123, Test@123",
        key="audit_test_passwords",
    )

    st.warning(
        "Never enter real account passwords. The report excludes "
        "actual password values, but the input is processed by the app."
    )

    if st.button("Generate Security Audit Report", type="primary"):

        passwords = [
            password.strip()
            for password in user_input.split(",")
            if password.strip()
        ]

        if not passwords:
            st.error("Please enter at least one fictional test password.")

        else:
            try:
                results = [
                    analyze_lab_password(password)
                    for password in passwords
                ]

                report_text = create_report(results)

                REPORTS_DIR.mkdir(parents=True, exist_ok=True)
                report_file = REPORTS_DIR / "security_audit_report.txt"

                report_file.write_text(
                    report_text,
                    encoding="utf-8",
                )

                weak = sum(
                    "weak" in item["strength"].lower()
                    for item in results
                )

                moderate = sum(
                    any(
                        word in item["strength"].lower()
                        for word in ["moderate", "medium", "fair"]
                    )
                    for item in results
                )

                strong = sum(
                    "strong" in item["strength"].lower()
                    for item in results
                )

                st.success("Security audit completed successfully!")

                col1, col2, col3, col4 = st.columns(4)
                col1.metric("Total Analyzed", len(results))
                col2.metric("Weak", weak)
                col3.metric("Moderate", moderate)
                col4.metric("Strong", strong)

                st.subheader("Individual Assessment Results")

                for index, item in enumerate(results, start=1):
                    with st.expander(f"Test Password #{index}"):
                        st.write(
                            f'**Length:** {item["length"]} characters'
                        )
                        st.write(f'**Strength:** {item["strength"]}')
                        st.write(f'**Score:** {item["score"]}')
                        st.write(
                            f'**Estimated Entropy:** {item["entropy"]}'
                        )

                        for recommendation in item["recommendations"]:
                            st.write(f"• {recommendation}")

                st.download_button(
                    "Download Security Audit Report",
                    data=report_text,
                    file_name="security_audit_report.txt",
                    mime="text/plain",
                )

                st.info(
                    "Report also saved in the project reports folder: "
                    f"{report_file}"
                )

            except Exception as error:
                st.error(f"Audit could not be completed: {error}")


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Password Security Assessment Suite | Educational Project | "
    "Fictional Test Data Only"
)
