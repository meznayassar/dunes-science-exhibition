import streamlit as st                                      # web app development
import pandas as pd                                         # for displaying table like data
from os import path, getcwd                                     
from PIL import Image
#----------------------------CSS Styling--------------------------

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

intro, events, exhibits, feedback, sponsors, credits,  contacts_us = st.tabs(["Introduction", "Events", "Exhibits", "Feedback", "Sponsors", "Credits", "Contact Us"])

with intro:
    st.header ("Welcome to Dunes Science Exhibition Portal")
    st.write('Blah '*200)
    st.markdown ("""
                 **Venue**: Dunes International School, Al-Khobar
                 
                 **Date**: December 2, 2023

                 **Time**: 9:00 AM - 5:00 PM
                 
                 """)
    st.map()

with events:
    st.table(pd.DataFrame({"Time":["09:00 - 10:00", "10:00 - 11:00", "11:00 - 12:00"], "Event":["Inaugration", "Award Ceremony", "Closing Ceremony"]}))

with exhibits:
    with st.expander("Grade 1"):
        st.markdown("""
                        <ol>
                        <li>ffffffffffffffffff</li>
                        <li>Bombastic Side eye</li>
                        <li>Just Looking Like a Wow</li>
                        <li>Blah Blah Blah</li>
                        </ol>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 2"):
        st.markdown("""
                         <ol> 
                         <li>Boom Shakalaka</li>
                         <li>Woof Woof</li>
                         <li>Baby Bhatuddoodo</li>
                         <li>Disco Party</li>
                         </ol>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 3"):
        st.markdown("""
                         <ol>
                         <li>Helicopter Helicopter</li>
                         <li>Bhupendra Jodi</li>
                         <li>Despacito</li>
                         </ol> 
                    """, unsafe_allow_html=True )
    with st.expander("Grade 4"):
        st.markdown("""
                         <ol>
                         <li>Shimmer</li>
                         <li>Cupcakes</li>
                         <li>Rocky</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 5"):
        st.markdown("""
                         <ol>
                         <li>Glow In The Dark</li>
                         <li>Puppets</li>
                         <li>Giraffes</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 6"):
        st.markdown("""
                         <ol>
                         <li>Slime</li>
                         <li>Nature</li>
                         <li>Rhinestones</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 7"):
        st.markdown("""
                         <ol>
                         <li>Rasberries</li>
                         <li>Candles</li>
                         <li>Pillows</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 8"):
        st.markdown("""
                         <ol>
                         <li>Snowflakes</li>
                         <li>Moons</li>
                         <li>Glitter</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 9"):
        st.markdown("""
                         <ol>
                         <li>Euphoria</li>
                         <li>Sunshine</li>
                         <li>Gentlecrabs</li>
                    """, unsafe_allow_html=True)
    with st.expander("Grade 10"):
        st.markdown("""
                         <ol>
                         <li>Celestial Bodies</li>
                         <li>Aura</li>
                         <li>Sway</li>
                    """, unsafe_allow_html=True)

with feedback:
    feedback_form_link = ''
    st.write("[Click here to submit](%s) feedback" % feedback_form_link)

with credits:
    developer, coordinator, project_owner = st.columns (3)

    with developer:
        st.subheader("Developer")
        # st.subheader("")
        # st.image(Image.open(path.join(dirname, "images", "mezu.png")))
        st.image("images/mezu1.png")
        st. write("Mezna Yassar")
    with coordinator:
        st.subheader("Site Co-ordinator")
        st.image("images/dhanu1.png")
        st. write("Dhanya Shyju")
    with project_owner:
        st.subheader("Principal")
        # st.subheader("")
        st.image("images/shazzu1.png")
        st. write("Shahzad Bilal")