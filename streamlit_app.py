import streamlit as st

create_page = st.Page("create.py", title="Create", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete", icon=":material/delete:")

pg = st.navigation(
    {
        "Actions": [create_page, delete_page],
    }
)
pg.run()

