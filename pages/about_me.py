import streamlit as st
from  forms.contact import contact_form

### -- Hero Section -- ##
col1, col2= st.columns(2,gap="small", vertical_alignment="center")
with col1 :
    st.image('WhatsApp Image 2024-08-16 at 20.31.23.jpeg')
with col2:
    st.title("CA Chetna Jain")
    st.write ("Incoming Charted Accountant. A intresting person trying to do a boring job.A bad person trying to lead a good lifestyle. Studious person 🤓 for continous 5 years now and loves nothing. ")
    if(st.button("✉️ Contact Me")):
        contact_form()


### Experience and Qualification

st.write("\n")
st.subheader("Experience and Qualification", anchor =False)
st.write("""
    - 19 years of experience in living the life
    - 19 years of experience in wasting life without any motive.
    - Donot know how to use social media properly.
    - 14 years of TMKOC fan. Still cannot find the Popatlal's wife.
    """)

st.write("\n")
st.subheader("Skills", anchor =False)
st.write("""
    - Speaking nonsense about anything in this world.
    - Compliments requirements continously.
    - Accounts and Economics Thoda sa.
    - Very low sense of humour.
    """)