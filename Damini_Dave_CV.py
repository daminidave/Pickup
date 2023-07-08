from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "DaminiDavePythonDeveloper.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Damini Dave"
PAGE_ICON = ":wave:"
NAME = "Damini Dave"
DESCRIPTION = """
Python developer with strong proficiency in Python programming, extensive experience in developing efficient and scalable
 solutions, and expertise in various Python frameworks and libraries. 
"""
EMAIL = "daminidave8@gmail.com"



st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
#profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    images = Image.open(current_dir / "assets" / "profile-pic.png")
    st.image(images, width=230)
    #newImage = image.resize((250, 250))
    #newimage = st.image(width=250)
    #st.image(newimage)

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



st.write('\n')
st.subheader("Summary")
st.write(
    """Experienced Python and C developer with 5.4 years of expertise in API development, backend programming, CI/CD pipeline management, and test automation. Skilled in creating visually rich dashboards using Streamlit and visualization libraries. Proficient in SQL and Python pandas for data manipulation and analysis. Proactive and independent team player with a track record of delivering successful projects.
"""
)
# --- HIGHLIGHTS ---
st.write('\n')
st.subheader("HIGHLIGHTS")
st.write(
    """
- ✔️ Proficient in Django and Flask framework.
- ✔️ Proficient in Object-Oriented Programming.
- ✔️ Strong Experience with Appium and Robot Framework for test automation.
- ✔️ Strong Skilled in working with relational databases, postgres and MySQL.
- ✔️ Strong Familiarity with various Python libraries/frameworks such as Regex, Pandas, Beautiful Soup, and Numpy.
- ✔️ Proficient in using Git, Bitbucket, JIRA, Pycharm, Gitlabee, Spyder, Confluence, and Docker for development and collaboration.

"""
)

# --- SKILLS AND COMPETENCIES---
st.write('\n')
st.subheader("SKILLS AND COMPETENCIES")
st.write(
    """
- 👩‍💻 Programming: Python(OOPs Concept,API development,Web Scraping,Pandas,numpy), C
- 📚 Framework: Django, Flask, Robot Framework,Streamlit,Android(Basic)
- 📊 Data Visualization: Streamlit, Seaborn,Matplotlib
- 🗄️ Databases: Postgres,  MySQL
- ☁   Cloud : Knowledge on AWS
-    Domain: Automotive, Telecommunication, Ecommerce

"""
)


# --- EMPLOYMENT HISTORY---
st.write('\n')
st.subheader("EMPLOYMENT HISTORY")
st.write(
    """
  1 .  Aricent/Altran/Capgemini, Bangalore, Karnataka
  
        Feb 2018 - July 2022
        Designation: [Consultant/Senior software engineer]


2. Deloitte, Bangalore, Karnataka

    July 2022 - Present
    Designation: [Consultant]

"""
)


# --- PROJECT EXPERIENCE ---
st.write('\n')
st.subheader("Project Experience")
st.write("---")

# --- PROJECT 1
st.write("**Project 1**")
st.write("🚧", "**Consultant | Deloitte Cortex AI**")
st.write(
    """
    - ► Involved in the design and development of APIs for Cortex AI, a platform for selling assets including data and physical devices. Created APIs for the marketplace, facilitating the sale of datasets, and the solution space, enabling the sale of services.
     - ► Utilized Django as the backend framework to design robust APIs with functionalities such as adding new assets, bookmarking assets, adding assets to cart, requesting assets, and providing feedback. 
    - ► Leveraged Postgres SQL as the database management system, ensuring efficient data storage and retrieval for the Cortex AI platform.  
    - ► Established a seamless flow of data in JSON format between the frontend and backend, optimizing communication and enabling efficient data exchange.
    - ► Implemented Python as the primary programming language for the development of the APIs, utilizing its extensive libraries and capabilities.
    - ► Utilized Postman for API testing, ensuring the reliability and functionality of the APIs in different scenarios."""

)

# --- Project 2
st.write('\n')
st.write("Project 2")
st.write("🚧", "**Consultant/Senior Software Engineer | Vendor BOM (POC)**")
st.write(
    """
    - ► Played a key role in designing APIs for chatbot implementation, for vendor BOM,enabling seamless integration and data retrieval for knowledge base queries from documents.
     - ► Developed APIs using Flask framework to ensure efficient and reliable communication between the chatbot and backend systems.
     - ► Utilized Python as the primary programming language for API development, leveraging its robust ecosystem and extensive libraries for effective implementation.
     - ► Employed Beautiful Soup for web scraping, extracting relevant information from various sources to enrich the chatbot's knowledge base.
     - ► Utilized MySql as the database management system, effectively handling data storage and retrieval for the chatbot application.
      """

)

# --- Project 3
st.write('\n')
st.write(" Project 3")
st.write("🚧", "**Consultant/Senior Software Engineer | Renault CCAR Infotainment System**")
st.write(
    """
    - ► Involved in writing automation scripts for Renault Infotainment System, focusing on features such as Air 
    Quality, Chassis, and Driving Eco, among others.
    - ► Utilized Robot and Appium frameworks for writing automation 
    scripts, incorporating Object-Oriented Programming (OOP) principles and leveraging the Pandas library for 
    efficient data handling.
    - ► Employed Xlrd and openpyxl libraries for Excel manipulation to generate reports, 
    including SRS import and re-import reports.
    - ► Played a key role in maintaining the CI/CD pipeline to ensure 
    smooth integration and deployment of automated scripts.
    - ► Led the automation team, providing guidance, 
    mentoring, and technical expertise, and successfully handled client calls to address requirements, updates, 
    and feedback. """
)

# --- Project 4
st.write('\n')
st.write("Project 4")
st.write("🚧", "**Consultant | MSI: WAVE7K PTT Server**")
st.write(
    """
    - ► Involved in writing new features like Embms for MSI wave 7k which is a push to talk device using python OOPS concept
    - ► Worked in project specific ootaa framework and wrote scripts for webscraping data into csv fiiles     
    - ► Worked in debugging and fixing bugs for server which was written in C++.
     ► Addition to fixing bugs in server also worked on fixing bugs for PTT App(Android App) which was written in Java 
     - ► Gained valuable experience in  utilizing and learning about the SIP protocol, widely used for call processing as well as used RTP and RTCP 
    protocol which is used for media floor transfer
     - ► Used Wireshark for troubleshooting and debugging """

)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader(" Proficiencies and Certification")
st.write("---")
st.write(
    """
    - ► Experience in handling client calls
    - ► Certification in web designing and development from INFOCAMPUS     
    - ► Android app development training from NETSPEQ solution 
    - ► Sound understanding of Automotive, Ecommerce and Telecom domain
     ► Participated in Hackathon"""

)
