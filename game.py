import mixaSV
import evgfun
import abrikos_bot
##import Seva_bot

f1 = mixaSV.mixaSV
f2 = abrikos_bot.abrikos_bot

def func1(history, n, table):
    return True

def func2(history, n, table):
    return False

table = [[(0, 0), (3, -1)], [(-1, 3), (2, 2)]]

def match(f1, f2, n):
    history = []
    
    for i in range(n):
        res1 = f1(history, 0, table)
        if res1 == 1:
            res1 = True
        elif res1 == 0:
            res1 = False
        res2 = f2(history, 1, table)
        if res2 == 1:
            res2 = True
        elif res2 == 0:
            res2 = False
        history.append((res1, res2))

    print(history)
##    sum1 = 0
##    sum2 = 0
##    for res in history:
##        if res[0] and res[1]

    
