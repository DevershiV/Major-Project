import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import extra_streamlit_components as stx
from pathlib import Path
from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)
for k, v in st.session_state.items():
    st.session_state[k] = v
current_pages = get_pages("Knowledgebase")
for key, value in current_pages.items():
    switch_page(value['page_name'])