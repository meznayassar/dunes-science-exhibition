import streamlit as st                                      # web app development
import pandas as pd                                         # for displaying table like data
from os import path, getcwd                                     
from PIL import Image
import base64
#----------------------------CSS Styling--------------------------

# st.set_page_config(layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        return base64.b64encode(image_file.read())

encoded_string = add_bg_from_local('images/stem3.png')    

st.markdown("""
        <style>

            .stTabs [aria-selected='true'] {
                color: #000000
            }

        </style>""", unsafe_allow_html=True)

st.write("""
        <style>

            button[data-baseweb='tab'] > div[data-testid='stMarkdownContainer] > p {
                font-size:15px
            }
        </style>""", unsafe_allow_html=True)

st.markdown("""
            <style>

            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}

            </style>""", unsafe_allow_html=True)

st.markdown("""
            <style>

            #GithubIcon {visibility: hidden;}
            
            <style>""", unsafe_allow_html=True)

st.markdown(f"""
            <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});

    }}
            </style>""", unsafe_allow_html=True)


#----------------------------School logo--------------------------

# get path to image in a variable named path_dunes_logo
# pass the image path to the function in streamlit that renders the image
st.image('images/dunes-logo1.png')

#----------------------------Tas and contents--------------------------

# create tabs that should appear on the web portal and save it in variables with names corresponding to the tabs
# using with statements, add content to the tab

# you can use st.write for displaying stuff on the page
#             st.map for maps
#             st.image to display images
#             st.columns to display stuff side by side and so on

intro, events, exhibits, gallery, credits,  contacts_us = st.tabs(["Introduction", "Events", "Exhibits", "Gallery", "Credits", "Contact Us"])

with intro:
    st.header ("Welcome to Dunes Science Exhibition Portal")
    st.write('*Welcome to the hub of brilliance, where science meets art in a symphony of innovation and creativity. Dive into the dynamic realm of our Dunes Science and Arts Exhibition, a fusion of intellect and imagination.*')
    st.write('*Unleash your curiosity as you explore the exhibits made with passion, each creation is a testament to the boundless potential within our talented students. We thank you for joining us on this thrilling journey of discovery!*')
    st.markdown ("""
                 **Venue**: Dunes International School, Al-Khobar
                 
                 **Date**: December 2, 2023

                 **Time**: 9:00 AM - 1:30 PM
                 
                 """)
    map = pd.read_excel('data/map.xlsx')
    st.map(map,latitude='lat', longitude='lon', zoom=15, color='#FF0000', size=20)

with events:
    st.write('**We invite all our guests to join us at the inaugral ceremony**')
    st.write('**09:30 - 10:00** - Inaugration Ceremony')
    st.write('**01:00 - 01:30** - Closing Ceremony')

    st.write('**                    **')
    st.write('**Our esteemed chief guests are**')
    st.write('Mr. Awad Al Qahtani')
    st.write('Ms. Sadaf Fahad ')
    st.write('Mr. Faisal Abdulla ')
    st.write('Mr. Khalid Al Owaid')

with exhibits:
    with st.expander("Science"):
        st.dataframe(pd.read_excel('data/Science.xlsx'), hide_index=True)

    with st.expander("Math"):
        st.dataframe(pd.read_excel('data/Math.xlsx'), hide_index=True)

               
    with st.expander("Social Science"):
        st.dataframe(pd.read_excel('data/Social.xlsx'), hide_index=True)

    with st.expander("Computer Science"):
        st.dataframe(pd.read_excel('data/Computer Science.xlsx'), hide_index=True)

    # with st.expander("English"):
    #     st.dataframe(pd.read_excel('data/English.xlsx'), hide_index=True)

    # with st.expander("Arts"):
    #     st.dataframe(pd.read_excel('data/Arts.xlsx'), hide_index=True)

# with feedback:
#     feedback_form_link = ''
#     st.write("[Click here to submit](%s) feedback" % feedback_form_link)

with credits:
    developer, coordinator, project_owner = st.columns (3)

    with developer:
        st.subheader("Developer")
        st.image("images/mezu1.png")
        st. write("Mezna Yassar")

    with coordinator:
        st.subheader("Site Co-ordinator")
        st.image("images/dhanu1.png")
        st. write("Dhanya Shyju")

    with project_owner:
        st.subheader("Academic Coordinator")
        st.image("images/shazzu1.png")
        st. write("Shahzad Bilal")