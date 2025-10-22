import streamlit as st
from  forms.contact import contact_form2
st.title("About my Brothers")

st.subheader("Deevyansh Khadria")
## -- Hero Section -- ##
col1,col2= st.columns(2,gap='small', vertical_alignment='center')
with col1:
    st.image('Screenshot 2024-08-17 at 3.15.12 PM.png')
with col2:
    st.title("Dumbass Engineer")
    st.write("He is a dumb engineer with the worst skills ever found on the planet. He is short tempered pokemon kind of person. He is intresting only in his dreams. He loves travelling and choclate cookies. He is ambivert not even trying to figure out his bad life.")
    if(st.button("✉️ Contact him?? Why?? are u mad or what?")):
        contact_form2()

st.write("\n")
st.subheader("Experience and Qualification")
st.write("""
    - He studies in Department of Electrical Engineering in the Indian Institute of Technology, Delhi.😪
    - He has handled my tanturms for 14 years. Pretty good at it.
    - He learned dance for 1 months and forgotten in 14 days. I know him he is mad.
    - He has experience of travelling different places (only the mountains 🥱)
    - What thats all.. these experiences are useless only
     """)

st.write("\n")
st.subheader("Skills")
st.write("""
    - Slow Typer... 😴
    - Slow at everything even slow than the tortoise.
    - Nothing , zero skills 
    - Doesnot sleeps at night kind aa pokemon owl.
    """)

