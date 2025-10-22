import streamlit as st

about_page=st.Page(
    page="pages/about_me.py",
    title="About Me",
    icon="👤",
    default=True
)
brothers_page=st.Page(
    page="pages/brothers.py",
    title="About My Brothers",
    icon="👬"
)
dashboard_page=st.Page(
    page="pages/dashboard.py",
    title="Gameboard",
    icon="📊"
)

collab=st.Page(
    page="pages/collab.py",
    title="Photo Collab",
    icon="📸"
)

## Shared on all the Pages ##
# st.logo("WhatsApp Image 2024-08-16 at 20.31.23.jpeg")
st.sidebar.text("Made with ❤️ by Deevyansh Khadria")





## -- Navigation setup -- ##
pg=st.navigation({
        "My Info": [about_page],
        "Others": [brothers_page, dashboard_page,collab]})
pg.run()

