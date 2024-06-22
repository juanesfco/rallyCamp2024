import pandas as pd
import datetime

def checkAlive():
    tab = pd.read_pickle('players.df')
    return(tab['alive'].sum())

def killPlayer(id):
    tab = pd.read_pickle('players.df')
    tab.loc[id,'alive'] = 0
    tab.to_pickle('players.df')

def revivePlayer(id):
    tab = pd.read_pickle('players.df')
    tab.loc[id,'alive'] = 1
    tab.loc[id,'opp'] = 'none'
    tab.loc[id,'pid'] = 'none'
    tab.to_pickle('players.df')

def resetTable():
    df = pd.read_csv('playersOriginal.csv')
    df['kills'] = [[]]*len(df)
    df.set_index('id',inplace=True)
    df.to_pickle('players.df')

def createChallenge(chalid,recid):
    pid = problemCount()
    tab = pd.read_pickle('players.df')
    tab.loc[chalid,'opp'] = recid
    tab.loc[recid,'opp'] = chalid
    tab.loc[chalid,'pid'] = str(pid)
    tab.loc[recid,'pid'] = str(pid)
    tab.to_pickle('players.df')
    df = pd.read_csv('problemsRally.csv')
    df.loc[int(pid),'chalid'] = chalid
    df.loc[int(pid),'recid'] = recid
    df.loc[int(pid),'used'] = 1
    df.to_csv('problemsRally.csv',index=False)
    

def problemCount(reset=False):
    if reset:
        f = open('problemCount.txt', 'w')
        f.write('-1')
        f.close()
        df = pd.read_csv('problemsRally.csv')
        df['used'] = [0]*len(df)
        df['chalid'] = ['none']*len(df)
        df['recid'] = ['none']*len(df)
        df['winid'] = ['none']*len(df)
        df.to_csv('problemsRally.csv',index=False)

    else:
        f = open('problemCount.txt', 'r')
        n = f.read()
        f.close()
        f = open('problemCount.txt', 'w')
        number = int(n)+1
        f.write('%d' % number)
        f.close()
        return number
    
def challenge(chalid,recid):
    players = pd.read_pickle('players.df')
    pid = players.loc[chalid,'pid']
    df = pd.read_csv('problemsRally.csv')
    return(df.loc[int(pid),'problemE'],pid)

def checkAnswer(pid,ans,userid,oppid):
    df = pd.read_csv('problemsRally.csv')
    players = pd.read_pickle('players.df')
    if df.loc[int(pid),'answer'] == ans:
        df.loc[int(pid),'winid'] = userid
        df.to_csv('problemsRally.csv',index=False)
        k = players.loc[userid,'kills'].copy()
        k.append(oppid)
        players.at[userid,'kills'] = k
        players.loc[oppid,'alive'] = 0
        players.to_pickle('players.df')
        return('Correct!')
    else:
        return('Wrong :(')
    
def checkIfDone(pid):
    df = pd.read_csv('problemsRally.csv')
    return(df.loc[int(pid),'winid'])

def cleanChallenge(userid):
    players = pd.read_pickle('players.df')
    players.loc[userid,'opp'] = 'none'
    players.loc[userid,'pid'] = 'none'
    players.to_pickle('players.df')

def readyForSurvival():
    now = datetime.datetime.now()
    r1s = datetime.datetime(2024,6,22,8,20)
    r1e = datetime.datetime(2024,6,22,15,30)

    r2s = datetime.datetime(2024,6,22,15,35)
    r2e = datetime.datetime(2024,6,22,15,45)

    r3s = datetime.datetime(2024,6,22,15,50)
    r3e = datetime.datetime(2024,6,22,16,0)

    r4s = datetime.datetime(2024,6,22,16,5)
    r4e = datetime.datetime(2024,6,22,16,15)

    r5s = datetime.datetime(2024,6,22,16,20)
    r5e = datetime.datetime(2024,6,22,16,30)

    r6s = datetime.datetime(2024,6,22,16,35)
    r6e = datetime.datetime(2024,6,22,16,45)

    if now < r1s:
        time = r1s - now
        return(str(time.seconds))
    elif now < r1e:
        return(1)
    elif now < r2s:
        time = r2s - now
        return(str(time.seconds))
    elif now < r2e:
        return(2)
    elif now < r3s:
        time = r3s - now
        return(str(time.seconds))
    elif now < r3e:
        return(3)
    elif now < r4s:
        time = r4s - now
        return(str(time.seconds))
    elif now < r4e:
        return(4)
    elif now < r5s:
        time = r5s - now
        return(str(time.seconds))
    elif now < r5e:
        return(5)
    elif now < r6s:
        time = r6s - now
        return(str(time.seconds))
    elif now < r6e:
        return(6)
    else:
        return(0)

def survival(pid):
    df = pd.read_csv('problemsSurvival.csv')
    return(df.loc[int(pid),'problemE'])

def checkIfDoneSurvival(pid):
    df = pd.read_csv('problemsSurvival.csv')
    return(df.loc[int(pid),'winid'])

def checkAnswerSurvival(pid,ans,userid):
    df = pd.read_csv('problemsSurvival.csv')
    if df.loc[int(pid),'answer'] == ans:
        df.loc[int(pid),'winid'] = userid
        df.to_csv('problemsSurvival.csv',index=False)
        revivePlayer(userid)
        return('Correct!')
    else:
        return('Wrong :(')

def readyForPerimeter():
    now = datetime.datetime.now()
    r1s = datetime.datetime(2024,6,22,8,30)
    r1e = datetime.datetime(2024,6,22,10,00)

    r2s = datetime.datetime(2024,6,22,15,55)
    r2e = datetime.datetime(2024,6,22,15,57)

    r3s = datetime.datetime(2024,6,22,16,20)
    r3e = datetime.datetime(2024,6,22,16,22)

    r4s = datetime.datetime(2024,6,22,16,45)
    r4e = datetime.datetime(2024,6,22,16,47)

    if now < r1s:
        time = r1s - now
        return(0,str(time.seconds))
    elif now < r1e:
        time = r1e - now
        return(1,str(time.seconds))
    elif now < r2s:
        time = r2s - now
        return(-1,str(time.seconds))
    elif now < r2e:
        time = r2e - now
        return(2,str(time.seconds))
    elif now < r3s:
        time = r3s - now
        return(-2,str(time.seconds))
    elif now < r3e:
        time = r3e - now
        return(3,str(time.seconds))
    elif now < r4s:
        time = r4s - now
        return(-3,str(time.seconds))
    elif now < r4e:
        time = r4e - now
        return(4,str(time.seconds))
    else:
        return(-4,-4)
    
def checkPeriComp(peri,userid):
    players = pd.read_pickle('players.df')
    col = 'p' + str(peri)
    return(players.loc[userid,col]==1)

def checkAnswerPeri(ans,peri,userid):
    df = pd.read_csv('perCheck.csv')
    players = pd.read_pickle('players.df') 
    if df.loc[int(peri)-1,'lid'] == ans:
        col = 'p' + str(peri)
        players.loc[userid,col] = 1
        players.to_pickle('players.df')
        return('Correct!')
    else:
        return('Wrong :(')
    
def eliminateNotPeri(userid):
    players = pd.read_pickle('players.df')
    col = 'p' + str(peri)
    return(players.loc[userid,col]==1)