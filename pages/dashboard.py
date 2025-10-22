import streamlit as st

st.title("Game board")
print("hello i am starting")

if "text" not in st.session_state:
    st.session_state.text = "Will u be my Sister??"
    st.session_state.counter = 0
    st.session_state.image = "pic1.jpg"

st.write(st.session_state.text)
st.image(st.session_state.image, width=350)

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

# --- YES Button ---
with col1:
    print("i am in col1", st.session_state.counter)
    if st.session_state.counter != 1:
        if st.button("Yes"):
            st.session_state.text = "Yess Lets party.."
            st.session_state.counter = 1
            st.session_state.image = "pic5.jpg"
            st.rerun()

# --- NO Button ---
with col2:
    print("i am in col2", st.session_state.counter)
    if st.session_state.counter!=-5 and st.session_state.counter!=1:
        no_clicked = st.button("No")  # only one 'No' button

        if no_clicked:
            if st.session_state.counter == 0:
                st.session_state.text = "Try one more time. Will u be my sister?"
                st.session_state.image = "pic6.jpg"
                st.session_state.counter = -1
            elif st.session_state.counter == -1:
                st.session_state.text = "Okkk!!! Take a breath. Lets try it again!! Will u be my sister?"
                st.session_state.image = "pic2.jpeg"
                st.session_state.counter = -2
            elif st.session_state.counter == -2:
                st.session_state.text = "Please Mann ja. Will u be my sister?"
                st.session_state.image = "pic3.jpg"
                st.session_state.counter = -3
            elif st.session_state.counter == -3:
                st.session_state.text = "Okk fine.. I am giving u one more chance. Will u be my sister?"
                st.session_state.image = "pic4.png"
                st.session_state.counter = -4
            else:
                st.session_state.text = "Now, its my turn"
                st.session_state.counter = -5
            st.rerun()
