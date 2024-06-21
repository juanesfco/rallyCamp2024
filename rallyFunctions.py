import pandas as pd

def checkAlive():
    tab = pd.read_pickle('players.df')
    return(tab['alive'].sum())

def killPlayer(id):
    tab = pd.read_pickle('players.df')
    tab.loc[id,'alive'] = 0
    tab.to_pickle('players.df')

def resetTable():
    tab = pd.read_pickle('players.df')
    tab.loc[:,'alive'] = 1
    tab.to_pickle('players.df')