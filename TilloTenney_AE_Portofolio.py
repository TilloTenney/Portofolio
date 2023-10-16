import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image

st.set_page_config(page_title="TilloTenney_AE_Webpage",page_icon=":memo:",layout="wide")

def load_anim(url):
    req = requests.get(url)
    return(req.json() if req.status_code == 200 else None)

def load_mail(url_2):
    req = requests.get(url_2)
    return(req.json() if req.status_code == 200 else None)

def local_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style.css")

lottie_anim = load_anim("https://lottie.host/51451734-dac8-4475-ad2f-5261c798bc50/5WKsGu6sR6.json") #Animation
lottie_anim_mail = load_mail("https://lottie.host/53c7b66a-6187-4ece-a8d9-d3a5737bb037/tMg9d4uwc2.json")
image_proj1 = Image.open("proj1.png")

with st.container():
    st.subheader("Hi, I'm Tillo Tenney A E :cyclone:")
    st.title("Skyrocketing 🚀 Data Sorcerer")
    st.write("Experienced Data Scientist with expertise in SQL Server admin, query optimization, data replication, SSIS, Python, ETL automation, and ML models, driving performance improvements and database efficiency.")
    st.markdown("[👉 :orange[Learn more]](https://www.linkedin.com/in/tillo-tenney-a-e-aspiring-datascientist/)")

with st.container():
    st.write("-----")
    left_col, right_col = st.columns(2)
    with left_col:
        st.header("My Area of Expertise")
        st.write("##") ##For new line
        st.write(
            """
            - Database Wizard: Elevating performance by 30% through SQL Server mastery.

            - Expert in Ensuring Data Consistency and Availability

            - Expert in SSIS for seamless data integration and ETL.

            - Expert in Python for Data Analysis, Visualization, and Manipulation.

            - Expert in successful Legacy server migrations at 98% accuracy for seamless transitions.

            - Expert in 95% optimized ETL flow automation for seamless, hands-free data processing.

            - Proven track record: Developing machine learning models with over 80% accuracy for data-driven decisions.

            - Database Efficiency Wizard: Recognized for advanced query optimization prowess.
            
            ✨ Uncover the enchantment in my Git repository – where expertise unveils boundless opportunities.
            """
        )

        st.write("[ 👉 :orange[Git]](https://github.com/TilloTenney/Projects_TilloTenney)")

    with right_col:
        st_lottie(lottie_anim,height=400,key="Data Scientist")

with st.container():
    st.write("----")
    st.header("My Project")
    st.write("##")
    image_column, text_column = st.columns(2)
    with image_column:
        st.image(image_proj1)
    with text_column:
        st.subheader("Youtube Harvesting")
        st.write(
            """
            - The world of YouTube is vast and filled with valuable data.
            
            - Our project aims to make managing that data as easy as possible.
            
            - We wanted to simplify this process by creating a user-friendly solution.
            """
        )
        st.markdown("[ 👉 :orange[Watch video]](https://youtu.be/w5qb9C7tfHA)")

with st.container():
    st.write("----")
    st.write("Slide into my DMs and let's make some conversational magic happen! 💬")
    st.write("##")

    contact = """
     <form action="https://formsubmit.co/tillotelay007@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder = "Your_name" required>
        <input type="email" name="email" placeholder = "Your_email" required>
        <input type="text" name="subject" placeholder = "Subject(Required)" required>
        <textarea name="message" placeholder = "Your message here" required></textarea>
        <button type="submit">Send</button>
     </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact, unsafe_allow_html=True)
    with right_column:
        st_lottie(lottie_anim_mail, height=300, key="Mail")
