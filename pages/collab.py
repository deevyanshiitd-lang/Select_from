import streamlit as st
st.title("Photo Collab")
options = ["🌍 Trip", "💖 Most Beautiful Person", "👸 White Princess", "🌸 Flowers"]
sel=st.select_slider("Select your emoji",options=options)
if(sel=="🌍 Trip"):
    st.image("Screenshot 2025-10-22 at 2.36.40 PM.png")
elif(sel=="💖 Most Beautiful Person"):
    st.image("Screenshot 2025-10-22 at 2.36.49 PM.png")
elif (sel == "👸 White Princess"):
    st.image("Screenshot 2025-10-22 at 2.37.07 PM.png")
elif (sel == "🌸 Flowers"):
    st.image("Screenshot 2025-10-22 at 2.53.35 PM.png")
