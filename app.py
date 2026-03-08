import streamlit as st
import subprocess
import tempfile

st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🐞"
)

st.title("🐞 AI Python Code Reviewer")
st.write("Analyze Python code and detect possible bugs with suggestions.")

# Code input
code = st.text_area(
    "🧑‍💻 Paste your Python code here",
    height=300,
    placeholder="Example:\n\nx = [1,2,3]\nprint(x[5])"
)

if st.button("Analyze Code"):

    if code.strip() == "":
        st.warning("Please enter Python code.")
    else:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp:

            temp.write(code.encode())
            temp_file = temp.name

        st.info("Running bug analysis...")

        result = subprocess.run(
            ["python", "-m", "pylint", temp_file],
            capture_output=True,
            text=True
        )

        st.subheader("🔎 Analysis Result")

        st.code(result.stdout)