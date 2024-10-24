import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()


def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()


login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

create_page = st.Page("create.py", title="Create", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete", icon=":material/delete:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Actions": [create_page, delete_page],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()
