import streamlit as st
import smtplib

## Extra Functions ##
@st.dialog("Contact Me")
def contact_form():
    with st.form("Contact Form"):
        name = st.text_input("First Name")
        email = st.text_input("Email")
        message = st.text_input("Message")
        submit_button= st.form_submit_button("Submit")

        if(submit_button):
            st.success("Message Sent")
            try :
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('deevyansh.iitd@gmail.com','fvay qntl tetx bdyo')
                str="Name -"+ name + "\nEmail -"+ email+ "\nMesaage -" + message
                server.sendmail("deevyansh.iitd@gmail.com", "deevyansh.iitd@gmail.com",str )
                server.quit()
            except:
                print("Email Not sent")

@st.dialog("Stop it!!!  He is Mad !! Contact My Brother")
def contact_form2():
    with st.form("Contact Form"):
        name = st.text_input("First Name")
        email = st.text_input("Email")
        message = st.text_input("Message")
        submit_button= st.form_submit_button("Submit")

        if(submit_button):
            st.success("Message Sent")
            try :
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('deevyansh.iitd@gmail.com','fvay qntl tetx bdyo')
                str="Name -"+ name + "\nEmail -"+ email+ "\nMesaage -" + message
                server.sendmail("deevyansh.iitd@gmail.com", "deevyansh.iitd@gmail.com",str )
                server.quit()
            except:
                print("Email Not sent")