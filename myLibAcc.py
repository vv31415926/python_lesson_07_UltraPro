import json
import os

def setAccount( persAcc, money, input=True ):
    rez = True
    if input == True:
        persAcc += money
    else:
        if  persAcc < money:
            rez = False
        else:
            persAcc -= money

    return persAcc, rez
# **********************************************

def setHistory( product, money, pers_acc, history, accept ):
    dic={}
    dic['step'] = product
    dic['money'] = str(money)
    dic['account'] = str(pers_acc)
    dic['accept'] = accept

    history.append( dic )
    return history
# **********************************************

def list_history( history ):
    lst = []
    for d in history:
        lst.append( d['step']+', '+d['money']+'руб., остаток:'+d['account']+'руб., - '+d['accept']  )
    return lst
# *********************************************

def getAccount( history ):
    if len( history ) > 0:
        d = history[-1]
        r = float( d['account'] )
    else:
        r = 0
    return r
# *********************************************

def read_history():
    if os.path.exists( 'history.json' ):
        with open( 'history.json', 'r' ) as f:
            history = json.load( f )
    else:
        history = []

    return history
# **********************************************

def write_history( h ):
    if len(h) > 0:
        with open( 'history.json', 'w' ) as f:
            json.dump( h, f  )
# **********************************************
