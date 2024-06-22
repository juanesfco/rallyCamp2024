import streamlit as st
import pandas as pd
import datetime
import os
import rallyFunctions as rf
from streamlit_autorefresh import st_autorefresh
from pytz import timezone

count = st_autorefresh(interval=1000, limit=5400)

st.markdown("""
<style>
section[data-testid="stSidebar"][aria-expanded="true"]{
display: none;
}
</style>
""", unsafe_allow_html=True)

col1,col2= st.columns(2)

with col1:
    if st.button("Logout"):
        st.switch_page("index.py")

with col2:
    if st.checkbox('Timer:'):
        countSec = int(int(count)/10)
        timer = str(datetime.timedelta(seconds=countSec))
        st.write(timer)

st.write("""
Mathematical Rally - OMPR Camp 2024
""")

st.write("""
Hunger Games Version:
""")

script_path = os.path.abspath(__file__)
user = os.path.basename(script_path)[:-3]

st.write("Hola ", user)

st.write("Current time", datetime.datetime.now(timezone('America/Barbados')))

if st.checkbox('Players Table:'):

    col3,col4,col5 = st.columns(3)
    with col3:
        if st.button('Reset Table:'):
            rf.resetTable()

    with col4:
        if st.checkbox('Kill Player:'):
            id = st.text_input('Enter id:')
            if st.button('Kill'):
                rf.killPlayer(id)

    with col5:
        if st.checkbox('Revive Player:'):
            id = st.text_input('Enter id:')
            if st.button('Revive'):
                rf.revivePlayer(id)

    tab = pd.read_pickle('players.df')
    st.table(tab)

if st.checkbox('Problem Table:'):
    prob = pd.read_csv('problemsRally.csv')
    f = open('problemCount.txt', 'r')
    n = f.read()
    f.close()

    col6,col7 = st.columns(2)
    with col6:
        st.write('Current problem: ',n)
    with col7:
        if st.button('Reset Problem Count'):
            rf.problemCount(True)
    st.table(prob)

if st.checkbox('Survival Table:'):
    sur = pd.read_csv('problemsSurvival.csv')
    if st.button('Reset Table'):
        sur.loc[:,'winid'] = ['none']*len(sur)
        sur.to_csv('problemsSurvival.csv',index=False)
    st.table(sur)

#if st.checkbox('Kill: '):
#    number = st.number_input("Insert a number: ",value=None)
#    if type(number) == float:
#        rf.killPlayer(number)

#if st.button('Reset game: '):
#    rf.resetTable()
    
#if st.checkbox('Check count: '):
#    st.write(count)
