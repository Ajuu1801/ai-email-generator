import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import pyperclip

# -------------------------------------------------
# LOAD ENV VARIABLES
# -------------------------------------------------
load_dotenv(dotenv_path=".env", override=True)
api_key = os.getenv("OPENAI_API_KEY")

# -------------------------------------------------
# INIT OPENAI CLIENT
# -------------------------------------------------
client = OpenAI(api_key=api_key)

# -------------------------------------------------
# STREAMLIT PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Email Generator",
    page_icon="📧",
    layout="centered"
)

st.title("📧 AI Email Generator")
st.caption("Generate professional emails using AI")

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "email" not in st.session_state:
    st.session_state.email = ""

if "subject" not in st.session_state:
    st.session_state.subject = ""

# -------------------------------------------------
# UI
# -------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    email_type = st.selectbox(
        "Email Type",
        ["Job Application", "Quotation", "Follow-up", "Leave Request", "Cold Email"]
    )

with col2:
    tone = st.selectbox(
        "Tone",
        ["Professional", "Friendly", "Formal"]
    )

length = st.radio(
    "Email Length",
    ["Short", "Medium", "Detailed"],
    horizontal=True
)

details = st.text_area(
    "Enter email details",
    placeholder="Example: Write a professional email saying the quotation is ready."
)

# -------------------------------------------------
# GENERATE EMAIL
# -------------------------------------------------
if st.button("✨ Generate Email"):
    if not api_key:
        st.error("API key not loaded.")
    elif not details.strip():
        st.warning("Please enter email details.")
    else:
        with st.spinner("Generating email..."):
            try:
                prompt = f"""
You are a professional business email writer.

Write a {tone}, {length} {email_type} email.
Include a subject line.

Details:
{details}

Format:
Subject: <subject>
Body:
<email body>
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=500
                )

                content = response.choices[0].message.content.strip()

                if "Subject:" in content and "Body:" in content:
                    subject_part, body_part = content.split("Body:", 1)
                    st.session_state.subject = subject_part.replace("Subject:", "").strip()
                    st.session_state.email = body_part.strip()
                else:
                    st.session_state.email = content

            except Exception as e:
                st.error(f"Error: {e}")

# -------------------------------------------------
# OUTPUT
# -------------------------------------------------
if st.session_state.email:
    st.subheader("📌 Subject")
    subject = st.text_input(
        "Edit subject if needed",
        value=st.session_state.subject
    )

    st.subheader("📨 Email Body")
    body = st.text_area(
        "Edit email before sending",
        value=st.session_state.email,
        height=260
    )

    email_text = f"Subject: {subject}\n\n{body}"

    colA, colB, colC = st.columns(3)

    # DOWNLOAD
    with colA:
        st.download_button(
            "⬇️ Download",
            email_text,
            file_name="email.txt"
        )

    # COPY
    with colB:
        if st.button("📋 Copy Email"):
            pyperclip.copy(email_text)
            st.success("Email copied to clipboard!")

    # CLEAR
    with colC:
        if st.button("🧹 Clear"):
            st.session_state.email = ""
            st.session_state.subject = ""
            st.rerun()
