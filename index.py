import streamlit as st
import pandas as pd
from datetime import datetime
import time
import rallyFunctions as rf
from streamlit_autorefresh import st_autorefresh

st.write(st.secrets['admin'])

#count = st_autorefresh(interval=500, limit=1000, key="fizzbuzzcounter")
 
st.write("""
Mathematical Rally - OMPR Camp 2024
""")

st.write("""
Hunger Games Version:
""")

#tab = pd.read_pickle('players.df')
#st.table(tab)
#if st.checkbox('Kill: '):
#    number = st.number_input("Insert a number: ",value=None)
#    if type(number) == float:
#        rf.killPlayer(number)

#if st.button('Reset game: '):
#    rf.resetTable()
    
#if st.checkbox('Check count: '):
#    st.write(count)

