#streamlit Portfolio by Jeffrey Fernandez 03/15/23
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Jeffrey Fernandez"
PAGE_ICON = ":wave:"
NAME = "Jeffrey Fernandez :wave:"
DESCRIPTION = """
Jeffrey is a Computer Scientist based in NYC with a passion for Data Engineering and software Developing.
"""
EMAIL = "ninjeff06@gmail.com | (929)-425-5178"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/jeffrey-fernandez-66857b269/",
    "GitHub": "https://github.com/wiggapony0925",
    "Twitter": "https://twitter.com/JeffreyF0925",
}
PROJECTS = {
    "🏆 Python Virus Building Simulation - graphing based on simulation": "https://github.com/wiggapony0925/Python-Virus-Building-Simulation-",
    "🏆 Python Password System - modules os & tkinter making user registration and log in system ": "https://github.com/wiggapony0925/Simply-python-password-system",
    "🏆  Stock Price Web App- StreamLit Web App": "https://github.com/wiggapony0925/Python-stock-web-app",
    "🏆 Portfolio - Custom Portfolio streamed with Render ": "https://github.com/wiggapony0925/Portfolio",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.info("Hello, I'm a programmer based in New York City", icon="ℹ️")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=350
             )

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ **AWS Cloud Computing** with Arizona State University 
- ✔️ College Level in my sophomore year Highschool of 2023
- ✔️ Good understanding data analysis and plotting using Numpy and Matplotlib **Jovian certification**
- ✔️ Recommendation to join **NASA CCRI internship for Volcanic Emission Impacts on Climate Systems**
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, JavaScript, Html, CSS, SQL
- 📊 Data Visulization:  MS Excel, Plotly, Streamlit, Python Modules **Matplotlib, and Pandas**
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**SEP INTERNSHIP | Web Design**")
st.write("02/2021-2022 - Present")
st.write(
    """
- ► Used skills to improve a NYC.gov website
"""
)

st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
