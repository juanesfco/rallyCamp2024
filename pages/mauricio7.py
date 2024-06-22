import streamlit as st
import pandas as pd
import os
import datetime
import rallyFunctions as rf
from streamlit_autorefresh import st_autorefresh
count = st_autorefresh(interval=1000, limit=5400)

st.markdown("""
<style>
section[data-testid="stSidebar"][aria-expanded="true"]{
display: none;
}
</style>
""", unsafe_allow_html=True)

if st.button("Logout"):
    st.switch_page("index.py")

st.write("""
Mathematical Rally - OMPR Camp 2024
""")

st.write("""
Hunger Games Version:
""")

script_path = os.path.abspath(__file__)
user = os.path.basename(script_path)[:-3]

st.write("Hi ", user)

tab = pd.read_pickle('players.df')
tabPlayer = tab[tab['user']==user]
userid = tabPlayer.index.values[0]
st.table(tabPlayer)

if tabPlayer.loc[userid,'alive'] == 1:
    peri,time = rf.readyForPerimeter()
    if peri == -4:
        st.write('No more perimeter checks.')
    elif peri > 0:
        if rf.checkPeriComp(peri,userid):
            st.write('Perimeter change completed.')
        else:
            body = 'WARNING: Perimeter check ends in ' + time + ' seconds.'
            st.warning(body)
            perQues = 'Enter code in perimeter locations #' + str(peri) + ':'
            answer = st.text_input(perQues)
            if st.button('Check code'):
                st.write(rf.checkAnswerPeri(answer,peri,userid))
    else:
        body = 'Next perimeter check in ' + time + ' seconds.'
        st.warning(body)
        if peri != 0:
            if not rf.checkPeriComp(-1*peri,userid):
                rf.killPlayer(userid)
        


    if tabPlayer.loc[userid,'opp'] == 'none':
        oppid = st.text_input('To start challenge enter opponent id: ')
        if st.button('Challenge!'):
            if tab.loc[oppid,'opp'] == 'none':
                rf.createChallenge(userid,oppid)
                st.stop()
            else:
                st.write("Id incorrect or opponent is already in a challenge.")
    else:

        oppid = tabPlayer.loc[userid,'opp']
        oppuser = tab.loc[oppid,'user']
        st.write("Challenge with ",oppuser)
        prob,pid = rf.challenge(userid,oppid)
        st.write(prob)
        if rf.checkIfDone(pid) == 'none':
            answer = st.text_input('Enter answer:')
            if st.button('Check answer'):
                st.write(rf.checkAnswer(pid,answer,userid,oppid))
        else:
            st.write('Challenge finished')
            rf.cleanChallenge(userid)
else:
    st.write('You are eliminated.')
    time = rf.readyForSurvival()
    if time == 0:
        st.write('No more survival problems.')
    elif type(time) == int:
        st.write('Survival Problem:')
        prob = rf.survival(time-1)
        st.write(prob)
        if rf.checkIfDoneSurvival(time-1) == 'none':
            answer = st.text_input('Enter answer:')
            if st.button('Check answer'):
                st.write(rf.checkAnswerSurvival(time-1,answer,userid))
    else:
        st.write('Next survival problem in ', time, ' seconds.')