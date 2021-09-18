import streamlit as st
from matchPage import show_match_page
from optPage import show_opt_page

page = st.sidebar.selectbox("Select an Option:", ('Coffee Chat Matches', 'Opt In/Out'))

if page == 'Coffee Chat Matches':
    show_match_page()
else:
    show_opt_page()
