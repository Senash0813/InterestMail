import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import os
import streamlit as st
from dotenv import load_dotenv


from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Decrypt .env.enc if running on Streamlit Cloud
if "DECRYPT_KEY" in st.secrets:
    decrypt_command = f"openssl aes-256-cbc -d -salt -pbkdf2 -in .env.enc -out .env -k {st.secrets['DECRYPT_KEY']}"
    os.system(decrypt_command)

# Load environment variables
load_dotenv()

# ✅ Move this line to the very top before any Streamlit functions
st.set_page_config(layout="wide", page_title="InterestMail", page_icon="📧")

# Apply Custom CSS
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 2.2em;
            font-weight: bold;
            color: #FF4B4B;
        }
        .stTextInput {
            width: 80%;
            margin: auto;
        }
        .stButton {
            display: flex;
            justify-content: center;
        }
        .success-message {
            font-size: 1.1em;
            color: green;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


def create_streamlit_app(llm, portfolio, clean_text):
    # Sidebar with App Description
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/732/732200.png", width=80)
        st.markdown("## InterestMail")
        st.write("Generate personalized emails for job opportunities by entering a job listing URL.")
        st.markdown("---")
        st.write("### How to Use:")
        st.write("1. Enter a **job listing URL**.")
        st.write("2. Click **Submit** to analyze the job.")
        st.write("3. View the **generated email** tailored to your skills.")

    # Main Title
    st.markdown('<h1 class="title">📧 InterestMail</h1>', unsafe_allow_html=True)

    # Centered Input and Button
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        url_input = st.text_input("Enter a Job URL:", value="https://careers.nike.com/junior-software-engineer/job/R-38916")
        submit_button = st.button("🔍 Generate Email")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                
                # Success Message
                st.markdown('<p class="success-message">✅ Email generated successfully!</p>', unsafe_allow_html=True)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"⚠️ An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    create_streamlit_app(chain, portfolio, clean_text)  # ✅ Keep this at the bottom
