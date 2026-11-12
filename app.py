import streamlit as st

import queries
from db import connect, reset

conn = connect()

st.title("Garden Beds")
st.write("Pick a page in the sidebar.")

st.caption(f"Logs with no bed: {queries.orphan_count(conn)}")

if st.button("Reset garden"):
    conn.close()
    reset()
    st.rerun()