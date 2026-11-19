
import os
from datetime import date

import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_openrouter import ChatOpenRouter

# ----------------------------------
# 1. Load environment variables
# ----------------------------------

load_dotenv(override=True)

api_key = os.getenv("OPENROUTER_API_KEY")
model_name = os.getenv("OPENROUTER_MODEL","openrouter/free")


# ----------------------------------
# 2. Streamlit page configuration
# ----------------------------------

st.set_page_config(
    page_title="Numera AI",
    page_icon="🔮",
    layout="centered"
)

# ----------------------------------
# 3. Custom UI styling
# ----------------------------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #101827, #202C45);
    color: #F3F4F6;
}

/* MAIN CONTENT */
.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* GENERAL TEXT */
.stApp p,
.stApp li,
.stApp label {
    color: #F3F4F6;
}

/* HEADINGS */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {
    color: #E8C780 !important;
}

/* AI GENERATED RESPONSE */
[data-testid="stMarkdownContainer"] {
    color: #F3F4F6 !important;
}

[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] strong {
    color: #F3F4F6 !important;
}

/* FORM CONTAINER */
[data-testid="stForm"] {
    background-color: #1B283A;
    border: 1px solid #43516A;
    border-radius: 16px;
    padding: 24px;
}

/* INPUT LABELS */
[data-testid="stWidgetLabel"] p {
    color: #F3F4F6 !important;
    font-weight: 600;
}

/* NAME INPUT */
[data-testid="stTextInput"] input {
    background-color: #25344B !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-radius: 8px;
}

/* INPUT PLACEHOLDER */
[data-testid="stTextInput"] input::placeholder {
    color: #AEB8C8 !important;
    -webkit-text-fill-color: #AEB8C8 !important;
}

/* DATE OF BIRTH INPUT */
[data-testid="stDateInput"] input {
    background-color: #25344B !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-radius: 8px;
}

/* DATE INPUT CONTAINER */
[data-testid="stDateInput"] [data-baseweb="input"] {
    background-color: #25344B !important;
}

/* DATE INPUT ICON */
[data-testid="stDateInput"] svg {
    color: #E8C780 !important;
    fill: none;
}

/* DATE PICKER POPUP */
div[data-baseweb="calendar"] {
    background-color: #1B283A !important;
    color: #FFFFFF !important;
}

/* CALENDAR TEXT */
div[data-baseweb="calendar"] button,
div[data-baseweb="calendar"] span,
div[data-baseweb="calendar"] div {
    color: #FFFFFF;
}

/* CALENDAR SELECTED DATE */
div[data-baseweb="calendar"]
button[aria-selected="true"] {
    background-color: #C6A35D !important;
    color: #101827 !important;
}

/* SPINNER */
[data-testid="stSpinner"] p,
[data-testid="stSpinner"] span {
    color: #E8C780 !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

/* GENERATE BUTTON */
.stButton button,
.stFormSubmitButton button {
    background-color: #C6A35D !important;
    color: #101827 !important;
    border-radius: 10px;
    font-weight: 700;
    border: none;
    padding: 12px;
}

/* BUTTON TEXT */
.stButton button p,
.stFormSubmitButton button p {
    color: #101827 !important;
}

/* BUTTON HOVER */
.stButton button:hover,
.stFormSubmitButton button:hover {
    background-color: #E8C780 !important;
    color: #101827 !important;
}

/* DOWNLOAD BUTTON */
.stDownloadButton button {
    background-color: #25344B !important;
    color: #E8C780 !important;
    border: 1px solid #C6A35D !important;
    border-radius: 10px;
}

/* DOWNLOAD BUTTON TEXT */
.stDownloadButton button p {
    color: #E8C780 !important;
}

/* CAPTIONS */
[data-testid="stCaptionContainer"] p {
    color: #BCC6D5 !important;
}

/* SUCCESS MESSAGE */
[data-testid="stAlert"] p {
    color: inherit;
}

/* DIVIDERS */
hr {
    border-color: #43516A !important;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------------
# 4. Application header
# ----------------------------------

st.markdown(
    "<h1 style='text-align:center;'>🔮 Numera AI</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:#BCC6D5;'>"
    "Discover your personality, strengths and life path"
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# ----------------------------------
# 5. User input
# ----------------------------------

st.subheader("✨ Discover Your Numerology")

with st.form("numerology_form"):

    name = st.text_input(
        "Your Name",
        placeholder="Enter your full name"
    )

    dob = st.date_input(
        "Date of Birth",
        value=date(1995, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    submitted = st.form_submit_button(
        "🔮 Generate My Reading",
        use_container_width=True
    )

# ----------------------------------
# 6. Prompt template
# ----------------------------------

prompt_template = PromptTemplate(
    input_variables=["name", "date_of_birth"],
    template="""
You are a friendly numerology expert.

Based on the following information:

Name: {name}
Date of Birth: {date_of_birth}

Generate a numerology-inspired reading with:

1. Life Path Number and calculation
2. Personality traits
3. Strengths and weaknesses
4. Career and relationship insights
5. Suggestions for personal improvement

Format the response using Markdown headings.
Keep the response engaging and easy to understand.

"""
)

# ----------------------------------
# 7. Initialize LLM and generate
# ----------------------------------

if submitted:

    if not name.strip():
        st.warning("Please enter your name.")

    elif not api_key:
        st.error(
            "OPENROUTER_API_KEY is missing from your .env file."
        )

    else:

        prompt = prompt_template.format(
            name=name.strip(),
            date_of_birth=dob.strftime("%d %B %Y")
        )

        try:
            with st.spinner("✨ Generating your reading..."):

                llm = ChatOpenRouter(
                    model=model_name,
                    temperature=0.7,
                    base_url="https://openrouter.ai/api/v1",
                    api_key=api_key,
                )

                response = llm.invoke(prompt)
            
              # Display model information
            metadata = response.response_metadata or {}

            actual_model = (
                metadata.get("model_name")
                or metadata.get("model")
                or model_name
            )

            st.success("Your reading is ready!")

            st.subheader("📜 Your Numerology Reading")
          
            st.subheader(f"🤖 Model: {actual_model}")
            st.markdown(response.content)

          

            # Download response
            st.download_button(
                "📥 Download Reading",
                data=str(response.content),
                file_name="numerology_reading.md",
                mime="text/markdown",
                use_container_width=True
            )

        except Exception as e:
            st.error(
                f"Unable to generate reading. "
                f"Error type: {type(e).__name__}"
            )

            # Detailed error in terminal logs
            print(
                f"LLM error: {type(e).__name__}: {e}"
            )

# ----------------------------------
# 8. Footer
# ----------------------------------

st.divider()

st.caption(
    "Built with Streamlit • LangChain • OpenRouter"
)

st.caption(
    "For entertainment and self-reflection only."
)
